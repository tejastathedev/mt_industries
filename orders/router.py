from fastapi import APIRouter, Depends
from orders.schema import CreatePaymentStatus
from database import Session
import service

# user_router = APIRouter(prefix='/user', tags=['user'])


# @user_router.post('/register')
# def register_user()


order_router = APIRouter(prefix='/order', tags=['order'])

@order_router.post('/')

def create_payment_status(request:CreatePaymentStatus, db: Session):
    return service.create_payment_status(request, db)

