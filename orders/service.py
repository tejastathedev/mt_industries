from database import Session
from datetime import datetime
from orders.schema import CreatePaymentStatus, OrderCreate
from orders.models import Order
from fastapi import HTTPException, status           



# create a payment status after payment is done 

def create_payment_status(request:CreatePaymentStatus,db : Session):

    payment = db.query(Payment).filter(payment.payment_id == request.payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.http_404_not_found, detail=f"Payment with id {request.payment_id} not found")
    
    new_payment_status = Payment(
        id=request.payment_id,
        payment_status=request.payment_status,
        payment_status_date=datetime.utcnow()
        )
    db.add(new_payment_status)
    db.commit()
    db.refresh(new_payment_status)
    return new_payment_status
    


    #nikita



def create_order_function(order: OrderCreate, db: Session):
    db_order = Order(**order.dict()) # Unpack the order data into the Order model
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

    