from products import models
from products.units.product_units_services import *
from products.units.prroduct_units_schema import CreateProductUnits, UnitResponse, DeleteProductUnits,  UpdateProductUnits
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from utils.response import Response


product_units_router = APIRouter(prefix="/product_units",tags=["Product Units"])

# Product Units Endpoints

# Create a new product unit
@product_units_router.post("/create/")
def create_product_unit(unit: CreateProductUnits, db: Session = Depends(get_db)):
    data =  create_units(db=db, schema=unit)
    return Response.generic_response(data=data,user_message="unit created successfully")



# Get all product units
@product_units_router.get("/get_all/")
def read_product_units(db: Session = Depends(get_db)): 
    d = get_units(db)
    return Response.generic_response(data=d,user_message="data fetch successfull")

# Soft delete a product unit by updating its status to 'deleted'
@product_units_router.delete("/delete/{unit_id}")
def delete_product_unit(unit_id: int, schema: DeleteProductUnits,db : Session = Depends(get_db)):
    return delete_unit(db, unit_id, schema)


# Update a product unit
@product_units_router.put("/update/{unit_id}")
def update_product_unit(unit_id, schema: UpdateProductUnits, db: Session = Depends(get_db)):
    return update_unit(db, unit_id, schema)






