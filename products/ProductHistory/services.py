from sqlalchemy.orm import Session
from fastapi import HTTPException
from products.ProductHistory import schemas
from products import models
import datetime,config
# from warehouse import models as WarehouseModel
from config import settings

def create_product_history(db:Session,product_id:int,warehouse_id:int):
    db_product=db.query(models.Products).filter(
        models.Products.id==product_id
    ).first()
    if not db_product:
        raise HTTPException(status_code=404,detail="Product Not Found in Product Table.!")
    
    db_history=db.query(models.ProductStockHistory).filter(
        models.ProductStockHistory.product_id==product_id,
        models.ProductStockHistory.warehouse_id==warehouse_id
    ).first()
    if db_history:
        raise HTTPException(status_code=404,detail="Product History Already Present.!")
    # db_warehouse=db.query(WarehouseModel.Warehouse).filter(
    #     WarehouseModel.Warehouse.id == warehouse_id
    # ).first()
    # if not db_warehouse:
    #     raise HTTPException(status_code=404,detail="Warehouse Not Found in Warehouse Table.!")
    db_history=models.ProductStockHistory(
        product_id = product_id,
        warehouse_id=warehouse_id,
        stock_type=settings.STOCK_TYPE[1],
        stock=db_product.initial_stock,
        prev_stock=10,  #this is temporary data
        current_stock=db_product.initial_stock-10, #this is temporary data
        status=settings.STATUS_ENUM[0],
        created_by=db_product.created_by,
        creation_date=db_product.creation_date,
        updated_by=db_product.updated_by,
        updation_date=db_product.updation_date,
        deleted_by=db_product.deleted_by,
        deletion_date=db_product.deletion_date
    )
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


def delete_product_history(db:Session,product_id:int,warehouse_id:int):
    db_history=db.query(models.ProductStockHistory).filter(
        models.ProductStockHistory.product_id==product_id,
        models.ProductStockHistory.warehouse_id==warehouse_id
    ).first()
    if not db_history:
        raise HTTPException(status_code=404,detail="Product History Already Deleted.!")
    
    db.delete(db_history)
    db.commit()
    return db_history