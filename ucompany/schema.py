from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from config import settings



#schemas for company 
class CompanyBase(BaseModel):
    name: str
    mail: EmailStr
    phone: str
    status: Optional[str] = settings.STATUS_ENUM[0]
    

class CompanyCreation(CompanyBase):
    created_by : int
    password:str
    creation_date:datetime

class Companyupdation(CompanyBase):
    password:str
    updated_by:int
    updation_date:datetime
    
class CompanyResponse(CompanyBase):
    id: int
    created_by:int
    creation_date: datetime

    class Config:
        orm_mode = True

