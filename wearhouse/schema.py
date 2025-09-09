from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from config import settings


class WarehouseBase(BaseModel):
    company_id: int
    latitude: float
    longitude: float
    address: str
    warehouse_name: str
    warehouse_manager: Optional[str] = None
    details: Optional[str] = None
    status: Optional[str] = settings.STATUS_ENUM[0]
   
class WarehouseCreate(WarehouseBase):
    created_by: int
    creation_date :datetime

class WarehouseUpdation(WarehouseBase):
    updated_by:int
    updation_date :datetime

class Warehousedeletion(BaseModel):
    deleted_by:int
    deletion_date :datetime

class WarehouseOut(WarehouseBase):
    id: int
    creation_date: datetime

    class Config:
        orm_mode = True
