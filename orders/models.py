from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Float, DateTime, func, Text
from sqlalchemy.orm import relationship, validates
from database import Base
from config import settings

# Columns that are common in most of the tables :-
# status, creation_date, created_by, updation_date, updated_by, deletion_time, deleted_by


# Orders table schema docs:
# Table Name : Orders
# ID -> PK, auto incremented
# Customer Related columns -> customer_name, customer_phone, customer_mail, customer_address, customer_remark
# Payment Related Columns -> payment_type, total_amount (calculated by order_products table)
# Order Related Columns - > platform_name, order_status
# Other misc columns -> admin_remark


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    customer_phone = Column(String(15), nullable=False)
    customer_mail = Column(String(255), nullable=False)
    customer_address = Column(String(500), nullable=False)
    platform_name = Column(String(255), nullable=False)
    order_payment_type = Column(
        Enum(*settings.ORDER_PAYMENT_TYPE, name="payment_enum"), nullable=False
    )
    total_amount = Column(Float, nullable=False)
    customer_remark = Column(String)
    admin_remark = Column(String)
    order_status = Column(
        Enum(*settings.ORDER_STATUS_ENUM, name="status_enum"), default=settings.ORDER_STATUS_ENUM[0]
    )
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # order_date = Column(DateTime, default=func.now(), nullable=False) #Removed the order date column as it was duplicated in creation date
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    order_products = relationship("OrderProduct", back_populates="order")


# order_products table schema docs:
# id : primary_key, autoincrement
# Relation with orders table:- order_id (referenced to orders.id)
# Relation with products table:- product_id (refernced to products.id)
# Base Product's price calculation :- product_purchase_price, quantity, total_amount (product_purchase_price * quantity)
# Discount Calculation :- discount(value not percentage), Using @validates to calculate discounted_amount
# Organizational benefits :- Profit_amount (store profit from [product_id.(selling_price - cost_price)*quantity])


class OrderProduct(Base):
    __tablename__ = "order_products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    # product_id = Column(Integer, ForeignKey("products.id"))
    product_purchase_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    discount = Column(Float, default=0.0)
    discounted_amount = Column(Float, default=0.0)
    profit_amount = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_products")
    product = relationship(
        "Products", back_populates="order_products"
    )

    @validates("discount")
    def calculate_discounted_amount(self, key, discount):
        self.discounted_amount = self.total_amount - discount
        return discount
