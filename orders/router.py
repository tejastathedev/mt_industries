from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from . import schema, services

user_router = APIRouter(prefix='/user', tags=['user'])
order_router = APIRouter(prefix='/orders', tags=['orders'])

# User endpoints
@user_router.post('/register')
def register_user():
    pass  # Implementation for user registration

# Orders endpoints
@order_router.post('/')
def create_order(order: schema.OrderCreate, db: Session = Depends(get_db)):
    return services.create_order(order, db)

# Update order status
@order_router.patch('/{order_id}/status')
def update_order_status(order_id: int, status: schema.Order_Status_Enum, db: Session = Depends(get_db)):
    return services.update_order_status(order_id, status, db)


# Get order details
@order_router.get('/{order_id}')
def get_order_details(order_id: int, db: Session = Depends(get_db)):
    return services.get_order_details(order_id, db)

# List all orders
@order_router.get('/')
def list_orders(db: Session = Depends(get_db)):
    return services.list_orders(db)
