from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from database import Base
from orders.schema import Constants

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    customer_mail = Column(String, nullable=False)
    customer_address = Column(String, nullable=False)
    platform_name = Column(String, nullable=False)
    payment_type = Column(Enum('COD', 'UPI', name='payment_enum'), nullable=False)
    total_amount = Column(Float, nullable=False)
    customer_remark = Column(String)
    admin_remark = Column(String)
    order_status = Column(Enum('ordered', 'delivered', 'cancelled', 'returned', name='order_status_enum'), default=Constants.ordered)