from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class ProductHistory(BaseModel):
    product_id: int
    warehouse_id: int

    stock_type:str
    stock: float
    prev_stock: float
    current_stock: float
    status:str

    created_by:Optional[int] 
    creation_date:Optional[date] | None=None
    updated_by:Optional[int] 
    updation_date:Optional[date] | None=None
    deleted_by:Optional[int]
    deletion_date:Optional[date] | None=None

class ProductHistoryResponse(ProductHistory):
    id:int

    class Config:
        from_attributes = True
