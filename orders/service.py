from database import Session
# from datetime import datetime
from orders.schema import OrderCreate
from orders.models import Order
# from fastapi import HTTPException, status           



# create a payment status after payment is done 

# def create_payment_status(request:CreatePaymentStatus,db : Session):

#     payment = db.query(Payment).filter(payment.payment_id == request.payment_id).first()
#     if not payment:
#         raise HTTPException(status_code=status.http_404_not_found, detail=f"Payment with id {request.payment_id} not found")
    
#     new_payment_status = Payment(
#         id=request.payment_id,
#         payment_status=request.payment_status,
#         payment_status_date=datetime.utcnow()
#         )
#     db.add(new_payment_status)
#     db.commit()
#     db.refresh(new_payment_status)
#     return new_payment_status
    


def create_order_function(order: OrderCreate, db: Session,status):
    db_order = Order(**order.dict()) # Unpack the order data into the Order model
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order



# Function to update order status

'''def update_order_status(order_id: int, status: schema.OrderStatusEnum, db: Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.order_status = status
    db.commit()
    db.refresh(db_order)
    return db_order'''

# Function to update stock after an order is placed

'''def update_stock(product_id: int, quantity: int, db: Session):
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    product.stock -= quantity
    db.commit()
    db.refresh(product)
    return product
'''
# Function to check low stock products

'''
def check_low_stock(db: Session):
    low_stock_products = db.query(Products).filter(Products.stock < 10).all()
    return low_stock_products'''


    