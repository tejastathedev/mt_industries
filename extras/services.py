from sqlalchemy.orm import Session
from extras.models import CompanyOTP
from random import choices
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from cron_jobs.otpJobs.models import OTPQueue
import smtplib
from email.message import EmailMessage

from utils.filtering import apply_filters


# OTP related Functions

def generateOTPFunc():
    otp = ''.join(choices('0123456789', k=4))
    print(otp)
    return otp

def updateOTP(company_id : int, otp : str, db : Session):

    filters = {
        'otp_companyid': company_id,

    }

    # otp_record = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    
    filters = {k: v for k, v in filters.items() if v is not None}

    query = db.query(CompanyOTP)
    query = apply_filters(query, filters)
    otp_record = query.first()# continue applying filter

    max_gen_hits = 3

    if otp_record:

        if(otp_record.creation_date is None):
            db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'creation_date' : datetime.now()})
        print("Creation Time: ",otp_record.creation_date)
        print("current time: ", datetime.now() )

        if otp_record.status == 'blocked':
            
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Please wait your status is blocked")
        
        if(otp_record.creation_date + timedelta(minutes=30) < datetime.now()):
            db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'generationHits': 0,'creation_date' : None, 'otp':otp})
        # check for generation hits
        if otp_record.generationHits < max_gen_hits:
            # increase generation hit and continue
            db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'generationHits' : otp_record.generationHits+1, 'otp' : otp})

            db.commit()
            return True
        # Check if this generation hit has been hit after 1 hour of (otp creation date), then 
        # Change the creation hit to current generation hit time !

        insert_otp_queue = OTPQueue(otp_id = otp_record.id, otp_creation_date = otp_record.creation_date)
        db.add(insert_otp_queue)
        db.commit()

        db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'status' : 'blocked'})
        db.commit()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="You cannot generate more than 3 otps at a time")
    otp_rec = CompanyOTP(company_id = company_id, otp = otp)
    db.add(otp_rec)
    db.commit()
    return True

def fetchOTP(company_id : int, db : Session):
    company_otp = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    if not company_otp:
        return None
    return company_otp.otp

def CompareOTP(company_otp : str, db_otp : str):
    if(db_otp != company_otp):
        return False
    return True

def IncreaseOTPHit(company_id, db: Session):
    company_otp = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    # Check has hits are already above threshold?
    max_hits = 3
    
    if company_otp.hits < max_hits:
        print("Hits are still less", company_otp.hits)
        # Check for the creation time and current time !

        if (company_otp.creation_date)+timedelta(minutes=30) < datetime.now():
            # OTP time is invalid
            return False
        # Increase Hit !
        db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({"hits" : company_otp.hits+1})
        db.commit()
        return True
    else:
        return False

def deleteOTPRecord(company_id : int, db : Session):
    record = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown error Occured, Generate OTP again")
    db.delete(record)
    db.commit()
    return True

# Captcha Related Functions

def captchaGeneration():
    captcha = ''.join(choices("abcdefghijklmnopqrstuvwxyz1234567890", k=6))
    return captcha

def temporaryUnbanFunction(company_id, db : Session):
    record = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    print(record.status)
    if not record.status == 'blocked':
        return False
    db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'status' : 'active', 'hits' : 0, 'generationHits': 0,'creation_date' : None})
    db.commit()
    return True


async def send_email(recipient_email : str, otp : str):
    # SMTP Config
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "eppsmanish@gmail.com"
    sender_password = "txff aklc bcru iovv"

    # Create the Email
    msg = EmailMessage()
    msg['Subject'] = "OTP (WMS)"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Body of the email
    msg.set_content(f"Please Enter the OTP to register! \n YOUR OTP: {otp} ")

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully!")
