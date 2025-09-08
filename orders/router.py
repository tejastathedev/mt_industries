from fastapi import APIRouter, Depends
from orders.schema import OrderCreate, OrderStatusEnum
from database import Session, get_db
from orders.models import Order
from .service import create_payment_status, create_order_function


# User endpoints
@user_router.post('/register')
def register_user():
    pass  # Implementation for user registration

# order_router = APIRouter(prefix='/order', tags=['order'])

# @order_router.post('/')

# def create_payment_status(request:CreatePaymentStatus, db: Session):
#     return service.create_payment_status(request, db)



#nikita

order_router = APIRouter(prefix='/orders', tags=['orders'])


# Orders endpoints
@order_router.post('/')
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order_function(order, db)



# Update order status
@order_router.patch('/{order_id}/status')
def update_order_status(order_id: int, status: OrderStatusEnum, db: Session = Depends(get_db)):
    return update_order_status(order_id, status, db)
