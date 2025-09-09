from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional
import config
# from sqlalchemy import Op
class RegisterProduct(BaseModel):
    name:str
    description:str
    img:str
    sku:str
    weight:float
    dimensions:str
    brand_name:str

    cost_price:float
    market_price:float
    selling_price:float
    initial_stock:float

    created_by:int
    updated_by:Optional[int]
    deleted_by:Optional[int]

    creation_date:Optional[date] | None=None
    updation_date:Optional[date] | None=None
    deletion_date:Optional[date] | None=None
 
    dimension_unit_id:int
    category_id:int
    weight_unit_id:int
    unit_id:int
    company_id:int



class RegisterProductResponse(RegisterProduct):
    id:int

    class Config:
        from_attributes = True 

class UpdateProduct(BaseModel):
    name:str
    description:str
    img:str
    sku:str
    weight:float
    dimensions:str
    brand_name:str

    cost_price:float
    market_price:float
    selling_price:float
    initial_stock:float

    created_by:int
    updated_by:Optional[int]
    deleted_by:Optional[int]

    updation_date:Optional[date] | None=None
    deletion_date:Optional[date] | None=None
 
    dimension_unit_id:int
    category_id:int
    weight_unit_id:int
    unit_id:int
    company_id:int

class UpdateProductResponse(UpdateProduct):
    id:int

    class Config:
        from_attributes = True 