from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from products.ProductHistory import schemas,services

producthistoryrouter=APIRouter(tags=["ProductsHistory"])

@producthistoryrouter.post("/RegisterProductHistory",response_model=schemas.ProductHistoryResponse)
def create_products_historys(product_id:int,warehouse_id:int,db:Session=Depends(get_db)):
    return services.create_product_history(db,product_id,warehouse_id)