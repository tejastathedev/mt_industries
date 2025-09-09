from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from config import settings

OrderStatusEnum = settings.OrderStatusEnum



class OrderBase(BaseModel):
    customer_name: str
    customer_phone: str
    customer_mail: str
    customer_address: str
    platform_name: str
    order_payment_type: str
    total_amount: float
    customer_remark: Optional[str]
    admin_remark: Optional[str]
    order_status: OrderStatusEnum = OrderStatusEnum.PENDING
    latitude: float
    longitude: float

class OrderCreate(OrderBase):
    pass


class OrderProductCreate(BaseModel):
    order_id : int
    product_id : int
    product_purchase_price : float
    quantity : int
    total_amount : float
    discount : Optional[float] = 0.0
    discounted_amount : Optional[float] = 0.0
    profit_amount : float



class OrderUpdate(BaseModel):
    order_status: Optional[OrderStatusEnum]
    admin_remark: Optional[str]

class Order(OrderBase):
    id: int
    creation_date: str
    created_by: Optional[int]
    updated_by: Optional[int]
    updation_date: Optional[str]
    deleted_by: Optional[int]
    deletion_date: Optional[str]

    class Config:
        orm_mode = True

class OrderProductBase(BaseModel):
    order_id: int
    product_id: int
    product_purchase_price: float
    quantity: int
    total_amount: float
    discount: Optional[float] = 0.0
    discounted_amount: Optional[float] = 0.0
    profit_amount: float

class OrderProductCreate(OrderProductBase):
    pass

class OrderProduct(OrderProductBase):
    id: int

    class Config:
        orm_mode = True

class Constants:
    # 'ordered', 'delivered', 'cancelled', 'returned'
    ordered = 'ordered'
    delivered = 'delivered'
    cancelled = 'cancelled'
    returned = 'returned'
  

# Changes made by nikita on 05092025
# Adding OrderProductUpdate schema to update quantity and discount
class OrderProductUpdate(BaseModel):
    product_id : Optional[int]
    quantity: Optional[int]
    discount: Optional[float]
    product_purchase_price: Optional[float]
    total_amount: Optional[float]
    profit_amount: Optional[float]
    discounted_amount: Optional[float]
    class Config:
        orm_mode = True
