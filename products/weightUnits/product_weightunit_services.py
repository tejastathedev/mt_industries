from ..models import WeightUnits
from ..weightUnits.product_weightunit_schema import CreateProductWeightUnit, UpdateProductWeightUnit, DeleteProductWeightUnit
from datetime import datetime
from fastapi import HTTPException
from config import settings

# Service functions for product weight units

# Create a new product weight unit
def create_weightunit(db, schema: CreateProductWeightUnit):
    # Check if a weight unit with the same name already exists and is not deleted
    existing_weightunit = db.query(WeightUnits).filter(
        WeightUnits.name == schema.name
    ).first()

    # If it exists, raise an HTTP 400 error
    if existing_weightunit:
        raise HTTPException(
            status_code=400,
            detail="Weight Unit with this name already exists."
        )
    # If it doesn't exist, create a new weight unit
    new_weightunit = WeightUnits(
        name=schema.name,
        created_by=schema.created_by,
        status=settings.STATUS_ENUM[0],
        creation_date=datetime.now()
    )

    db.add(new_weightunit)
    db.commit()
    db.refresh(new_weightunit)  # ← necessary to get the auto-generated ID

    return new_weightunit  # This matches response_model=weightUnitResponse


# Retrieve all product weight units
def get_weightunits(db):
    weightunits=db.query(WeightUnits).all()
    if not weightunits:
        return []
    return weightunits


# Soft delete a product weight unit by updating its status to 'deleted'
def delete_weightunit(db, weightunit_id: int, schema: DeleteProductWeightUnit):
    weightunit = db.query(WeightUnits).filter(WeightUnits.id == weightunit_id).first()
    if not weightunit:
        raise HTTPException(status_code=404, detail="Weight Unit not found")
    weightunit.deleted_by = schema.deleted_by
    weightunit.deletion_date = datetime.now()
    weightunit.status = settings.STATUS_ENUM[1]  #'deleted' is the second status in the list
    db.commit()
    return "Weight Unit deleted successfully"


# Update an existing product weight unit
def update_weightunit(db, weightunit_id :int, schema: UpdateProductWeightUnit):
    weightunit = db.query(WeightUnits).filter(WeightUnits.id == weightunit_id).first()
    if not weightunit:
        raise HTTPException(status_code=404, detail="Weight Unit not found")
    
    # Check if a weight unit with the new name already exists and is not deleted
    existing_weightunit = db.query(WeightUnits).filter(
        WeightUnits.name == schema.name, 
        WeightUnits.status != 'deleted',
        WeightUnits.id != weightunit_id  # Exclude the current weight unit from the check
    ).first()

    # If it exists, raise an HTTP 400 error
    if existing_weightunit:
        raise HTTPException(
            status_code=400,
            detail="Weight Unit with this name already exists."
        )
    
    weightunit.name = schema.name
    weightunit.updated_by = schema.updated_by
    weightunit.update_date = datetime.now()
    
    db.commit()
    db.refresh(weightunit)
    
    return weightunit


# 


