from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

#schemas for UserScope

class UserScope(BaseModel):
    scope_name: str

class ScopeResponse():
    id:int

    class Config:
        orm_mode = True





#schemas for company 
class CompanyBase(BaseModel):
    name: str
    mail: EmailStr
    phone: str
    status: Optional[str] = None
    

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


#schemas for wearhouse

class WarehouseBase(BaseModel):
    company_id: int
    latitude: float
    longitude: float
    address: str
    warehouse_name: str
    warehouse_manager: Optional[str] = None
    details: Optional[str] = None
    status: Optional[str] = None

class WarehouseCreate(WarehouseBase):
    created_by: int

class WarehouseOut(WarehouseBase):
    id: int
    creation_date: datetime

    class Config:
        orm_mode = True


#schemas for User 
class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    scope_id: int
    company_id: int
    status: Optional[str] = None

class UserCreate(UserBase):
    mail: EmailStr
    password: str
    created_by: int
    creation_date:datetime

class UserUpdate(UserBase):
    password:str
    updated_by:int
    updation_date:datetime



class UserResponse(UserBase):
    id: int
    creation_date: datetime

    class Config:
        orm_mode = True
