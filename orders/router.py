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
def update_order_status(order_id: int, status: schema.OrderStatusEnum, db: Session = Depends(get_db)):
    return services.update_order_status(order_id, status, db)



# changes made by nikita on 05092025 13:37
# Update stock after an order is placed
@order_router.post('/{product_id}/update-stock')    
def update_stock(product_id: int, quantity: int, db: Session = Depends(get_db)):
    return services.update_stock(product_id, quantity, db)
# Check low stock products
@order_router.get('/low-stock')
def check_low_stock(db: Session = Depends(get_db)):
    return services.check_low_stock(db)
#05092025 Adding restock endpoint
# Restock a product
@order_router.post('/{product_id}/restock')
def restock_product(product_id: int, additional_stock: int, db: Session = Depends(get_db)):
    return services.restock_product(product_id, additional_stock, db)
# Get order details
@order_router.get('/{order_id}')
def get_order_details(order_id: int, db: Session = Depends(get_db)):
    return services.get_order_details(order_id, db)

# List all orders
@order_router.get('/')
def list_orders(db: Session = Depends(get_db)):
    return services.list_orders(db)
    return orders
