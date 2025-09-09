from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Baseclass(BaseModel):
    email:str
    otp_code :str
    created_at : datetime

