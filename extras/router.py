from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from extras.services import generateOTPFunc, updateOTP, fetchOTP, CompareOTP, IncreaseOTPHit, deleteOTPRecord, captchaGeneration
from extras.schema import OTPSchema, GetOTP, CaptchaSchema


extra_router = APIRouter(prefix="/ex", tags=['ex'])

@extra_router.post('/getOTP')
def generateOTP(company : GetOTP, db : Session = Depends(get_db)):
    otp = generateOTPFunc()
    updateOTP(company.company_id, otp, db)
    return {
        "otp" : otp
    }


@extra_router.post('/validateotp')
def validateOTP(otp : OTPSchema, db : Session = Depends(get_db)):
    db_otp = fetchOTP(otp.company_id, db)
    if not db_otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please Generate the OTP again")
    if not CompareOTP(otp.company_otp, db_otp):
        # Increase hit and Return Wrond OTP inserted
        can_increased = IncreaseOTPHit(otp.company_id, db)
        if not can_increased:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Max Tries reached or time is invalid, Generate another OTP")
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="OTP does not match")
    
    # Delete the otp record so that this otp cannot be used again
    deleteOTPRecord(otp.company_id, db)
    return {"message" : "OTP validated"}


# Captcha Endpoints 
@extra_router.get('/getcapthca')
def GetCaptcha():
    captcha = captchaGeneration()
    return {
        "captcha" : captcha
    }

@extra_router.post('/validateCaptcha')
def validateCaptcha(user_captcha : CaptchaSchema):
    if(user_captcha.captcha_typed == user_captcha.original_captcha):
        return {'message' : "Captcha Verified"}
    return {'message' : "Filled Captcha is Wrong"}
    
