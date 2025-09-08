from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schema
from products.models import Products

# Function to create a new order
def create_order(order: schema.OrderCreate, db: Session):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Function to update order status
def update_order_status(order_id: int, status: schema.OrderStatusEnum, db: Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.order_status = status
    db.commit()
    db.refresh(db_order)
    return db_order

# Function to update stock after an order is placed
def update_stock(product_id: int, quantity: int, db: Session):
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    product.stock -= quantity
    db.commit()
    db.refresh(product)
    return product

# Function to check low stock products
def check_low_stock(db: Session):
    low_stock_products = db.query(Products).filter(Products.stock < 10).all()
    return low_stock_products
