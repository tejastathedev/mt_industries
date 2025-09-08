from pydantic import BaseModel

class OTPSchema(BaseModel):
    company_otp : str
    company_id : int

class GetOTP(BaseModel):
    company_id : int

class CaptchaSchema(BaseModel):
    captcha_typed : str
    original_captcha : str

class UnbanSchema(BaseModel):
    company_id : int