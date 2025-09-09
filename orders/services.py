from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schema
from products.models import Products

# Function to create a new order
def create_order(order: schema.OrderCreate, db: Session):
    db_order = models.Order(**order.dict()) # Unpack the order data into the Order model
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Function to update order status
def update_order_status(order_id: int, status: schema.Order_Status_Enum, db: Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first() # Fetch the order by ID
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.order_status = status
    db.commit()
    db.refresh(db_order)
    return db_order

 
# Function to get order details
def get_order_details(order_id: int, db: Session):  
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first() # Fetch the order by ID
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
# Function to list all orders
def list_orders(db: Session):
    orders = db.query(models.Order).all() # Fetch all orders
    return orders

