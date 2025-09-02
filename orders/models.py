from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Float, DateTime, func
from sqlalchemy.orm import relationship, validates
from database import Base
from orders.schema import Constants

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    customer_phone = Column(String(15), nullable=False)
    customer_mail = Column(String(255), nullable=False)
    customer_address = Column(String(500), nullable=False)
    platform_name = Column(String(255), nullable=False)
    payment_type = Column(Enum('COD', 'UPI', name='payment_enum'), nullable=False)
    total_amount = Column(Float, nullable=False)
    customer_remark = Column(String)
    admin_remark = Column(String)
    order_status = Column(Enum('ordered', 'delivered', 'cancelled', 'returned', name='order_status_enum'), default=Constants.ordered)
    order_date = Column(DateTime, default=func.now(), nullable=False)
    status = Column(Enum('live', 'deleted', name='order_status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime)

    orderproducts = relationship('OrderProduct', back_populates='order')
    
    created_by_user = relationship('User', foreign_keys=[created_by])
    updated_by_user = relationship('User', foreign_keys=[updated_by])
    deleted_by_user = relationship('User', foreign_keys=[deleted_by])

class OrderProduct(Base):
    __tablename__ = 'orderproducts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    product_purchase_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    discount = Column(Float, default=0.0)
    discounted_amount = Column(Float, default=0.0)
    profit_amount = Column(Float, nullable=False)

    order = relationship('Order', back_populates='orderproducts')
    product = relationship('Product', back_populates='orderproducts', foreign_keys=[product_id])

    @validates('discount')
    def calculate_discounted_amount(self, key, discount):
        self.discounted_amount = self.total_amount - discount
        return discount
