from products import models
from .product_services import *
from .schema import CreateProductUnits, UnitResponse, DeleteProductUnits,  UpdateProductUnits
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db


product_units_router = APIRouter(prefix="/product_units",tags=["Product Units"])

# Product Units Endpoints

# Create a new product unit
@product_units_router.post("/create/", response_model=UnitResponse)
def create_product_unit(unit: CreateProductUnits, db: Session = Depends(get_db)):
    return create_units(db=db, schema=unit)


# Get all product units
@product_units_router.get("/get_all/")
def read_product_units(db: Session = Depends(get_db)): 
    return get_units(db)


# Get a product unit by its ID
@product_units_router.get("/get/{unit_id}", response_model=UnitResponse)
def read_product_unit(unit_id :int, db : Session = Depends(get_db)):
    return get_unit_by_id(unit_id,db)


# Soft delete a product unit by updating its status to 'deleted'
@product_units_router.delete("/delete/{unit_id}", response_model=UnitResponse)
def delete_product_unit(unit_id: int, schema: DeleteProductUnits,db : Session = Depends(get_db)):
    return delete_unit(db, unit_id, schema)


# Update a product unit
@product_units_router.put("/update/{unit_id}",response_model=UnitResponse)
def update_product_unit(unit_id, schema: UpdateProductUnits, db: Session = Depends(get_db)):
    return update_unit(db, unit_id, schema)






