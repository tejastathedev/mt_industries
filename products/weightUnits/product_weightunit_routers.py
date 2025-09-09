from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from products.weightUnits import product_weightunit_schema, product_weightunit_services


weightunit_router = APIRouter(prefix="/weightunits", tags=["Product Weight Units"])

# Create a new product weight unit
@weightunit_router.post("/create",)
def create_product_weightunit(schema: product_weightunit_schema.CreateProductWeightUnit, db: Session = Depends(get_db)):
    return product_weightunit_services.create_weightunit(db, schema)


# Retrieve all product weight units
@weightunit_router.get("/getall")
def get_weightunits(db: Session = Depends(get_db)):
    return product_weightunit_services.get_weightunits(db)


# Soft delete a product weight unit by updating its status to 'deleted'
@weightunit_router.delete("/delete/{weightunit_id}")
def delete_weightunit(weightunit_id: int, schema: product_weightunit_schema.DeleteProductWeightUnit, db: Session = Depends(get_db)):
    return product_weightunit_services.delete_weightunit(db, weightunit_id, schema)

# Update an existing product weight unit
@weightunit_router.put("/{weightunit_id}", response_model=product_weightunit_schema.weightUnitResponse)
def update_weightunit(weightunit_id: int, schema: product_weightunit_schema.UpdateProductWeightUnit, db: Session = Depends(get_db)):
    return product_weightunit_services.update_weightunit(db, weightunit_id, schema)

