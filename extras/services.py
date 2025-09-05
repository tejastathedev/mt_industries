from sqlalchemy.orm import Session
from extras.models import CompanyOTP
from random import choices
from fastapi import HTTPException, status

def generateOTPFunc():
    otp = ''.join(choices('0123456789', k=4))
    print(otp)
    return otp

def updateOTP(company_id : int, otp : str, db : Session):
    otp_record = db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).first()
    max_gen_hits = 3
    
    if otp_record:

        if otp_record.status == 'blocked':
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Please wait your status is blocked")
    
        # check for generation hits
        if otp_record.generationHits < max_gen_hits:
            # increase generation hit and continue
            db.query(CompanyOTP).filter(CompanyOTP.company_id == company_id).update({'generationHits' : otp_record.generationHits+1})
            db.commit()
            return True
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
        # if (company_otp.creation_date)+timedelta(minutes=30) < datetime.now():
        #     # OTP time is invalid
        #     return False
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