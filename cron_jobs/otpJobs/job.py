from cron_jobs.otpJobs.models import OTPQueue
from datetime import datetime, timedelta
from extras.models import CompanyOTP


from database import sessionLocal  # assuming SessionLocal = sessionmaker(bind=engine)

def unbanUserOTP():
    # print("Running")
    db = sessionLocal()
    try:
        records = db.query(OTPQueue).all()
        for record in records:
            if record.otp_creation_date + timedelta(seconds=30) < datetime.now():
                print("unbanning the id: ", record.otp_id, " having creation time: ", record.otp_creation_date)
                db.query(CompanyOTP).filter(CompanyOTP.id == record.otp_id).update({
                    'status': 'active',
                    'hits': 0,
                    'generationHits': 0,
                    'otp' : 0000,
                    'creation_date': None
                })
                db.delete(record)
        db.commit()
    except Exception as e:
        print(f"Error during unbanUserOTP: {e}")
        db.rollback()
    finally:
        db.close()


