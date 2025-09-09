from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from products.dimensionUnits import dimensionunit_schema, dimensionunit_services


dimension_router = APIRouter(prefix="/dimensionunits",tags=["Product Dimension Units routes"])

# Create a new product dimension unit
@dimension_router.post("/create/", response_model=dimensionunit_schema.DimensionUnitsResponse)
def create_product_dimensionunit(schema: dimensionunit_schema.CreateDimensionUnits, db: Session = Depends(get_db)):
    return dimensionunit_services.create_dimensionunit(db, schema)

# Retrieve all product dimension units
@dimension_router.get("/getall/")
def get_product_dimensionunits(db: Session = Depends(get_db)):
    return dimensionunit_services.get_dimensionunits(db)

# Soft delete a product dimension unit by updating its status to 'deleted'
@dimension_router.delete("/delete/{dimensionunit_id}")
def delete_product_dimensionunit(dimensionunit_id: int, schema: dimensionunit_schema.DeleteDimensionUnits, db: Session = Depends(get_db)):
    return dimensionunit_services.delete_dimensionunit(db, dimensionunit_id, schema)

# Update an existing product dimension unit
@dimension_router.put("/update/{dimensionunit_id}", response_model=dimensionunit_schema.DimensionUnitsResponse)
def update_product_dimensionunit(dimensionunit_id: int, schema: dimensionunit_schema.UpdateDimensionUnits, db: Session = Depends(get_db)):
    return dimensionunit_services.update_dimensionunit(db, dimensionunit_id, schema)

