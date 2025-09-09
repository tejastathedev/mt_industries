from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from products import schemas,services

productrouter=APIRouter(tags=["Products"])

@productrouter.post("/RegisterProduct",response_model=schemas.RegisterProductResponse)
def create_productss(products:schemas.RegisterProduct,db:Session=Depends(get_db)):
    return services.create_product(db,products)

@productrouter.put("/UpdateProduct",response_model=schemas.RegisterProductResponse)
def update_productss(product_id:int,product_name:str,products:schemas.RegisterProduct,db:Session=Depends(get_db)):
    return services.update_product(db,products,product_id,product_name)

@productrouter.delete("/DeleteProduct",response_model=schemas.RegisterProductResponse)
def delete_productss(product_id:int,product_name:str,deleted_by:int,db:Session=Depends(get_db)):
    return services.delete_product(db,product_id,product_name,deleted_by)

@productrouter.get("/ShowAllProducts/{company_id}", response_model=list[schemas.RegisterProductResponse])
def show_all_productss(company_id: int, db: Session = Depends(get_db)):
    return services.show_all_products(db, company_id)
