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

#
def OrderProductStockDetails(order_id: int, db: Session):
    order_products = db.query(models.OrderProduct).filter(models.OrderProduct.order_id == order_id).all()
    return order_products

# Function to update order status
def update_order_status(order_id: int, status: schema.Order_Status_Enum, db: Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first() # Fetch the order by ID
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.order_status = status
    db.commit()
    db.refresh(db_order)
    return db_order

# Function to update stock after an order is placed
def update_stock(product_id: int, quantity: int, db: Session):
    product = db.query(Products).filter(Products.id == product_id).first() # Fetch the product by ID
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
    low_stock_products = db.query(Products).filter(Products.stock < 10).all() # Assuming low stock threshold is 10
    return low_stock_products


#05092025 Adding restock function
# Function to restock a product
def restock_product(product_id: int, additional_stock: int, db: Session):   
    product = db.query(Products).filter(Products.id == product_id).first() # Fetch the product by ID
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.stock += additional_stock
    db.commit()
    db.refresh(product)
    return product  
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
# # Function to delete an order
# def delete_order(order_id: int, db: Session):
#     db_order = db.query(models.Order).filter(models.Order.id == order_id).first() # Fetch the order by ID
#     if not db_order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     db.delete(db_order)
#     db.commit()
#     return {"detail": "Order deleted successfully"}
# Function to add products to an order
def add_product_to_order(order_product: schema.OrderProductCreate, db: Session):
    db_order_product = models.OrderProduct(**order_product.dict()) # Unpack the order product data into the OrderProduct model
    db.add(db_order_product)
    db.commit()
    db.refresh(db_order_product)
    return db_order_product
# Function to list products in an order
def list_order_products(order_id: int, db: Session):
    order_products = db.query(models.OrderProduct).filter(models.OrderProduct.order_id == order_id).all() # Fetch products by order ID
    return order_products

# Function to update product quantity in an order
def update_order_product_quantity(order_product_id: int, new_quantity: int, db: Session
):
    db_order_product = db.query(models.OrderProduct).filter(models.OrderProduct.id == order_product_id).first() # Fetch the order product by ID
    if not db_order_product:
        raise HTTPException(status_code=404, detail="Order product not found")
    if new_quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")
    product = db.query(Products).filter(Products.id == db_order_product.product_id).first()
    if product.stock < new_quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock for the product")
    db_order_product.quantity = new_quantity
    db.commit()
    db.refresh(db_order_product)
    return db_order_product
