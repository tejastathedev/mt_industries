from ..models import Units
from products.units.prroduct_units_schema import CreateProductUnits, UpdateProductUnits, DeleteProductUnits
from datetime import datetime
from fastapi import HTTPException
from config import settings

# Service functions for product units

# Create a new product unit
def create_units(db, schema: CreateProductUnits):
    # Check if a unit with the same name already exists and is not deleted
    existing_unit = db.query(Units).filter(
        Units.name == schema.name, Units.status != 'deleted'
    ).first()

    # If it exists, raise an HTTP 400 error
    if existing_unit:
        raise HTTPException(
            status_code=400,
            detail="Unit with this name already exists."
        )
    # If it doesn't exist, create a new unit
    new_unit = Units(
        name=schema.name,
        created_by=schema.created_by,
        status=settings.STATUS_ENUM[0],
        creation_date=datetime.now()
    )

    db.add(new_unit)
    db.commit()
    db.refresh(new_unit)  # ← necessary to get the auto-generated ID

    return new_unit  # This matches response_model=UnitResponse


# Retrieve all product units
def get_units(db):
    units=db.query(Units).all()
    if not units:
        return []
    return units



# Soft delete a product unit by updating its status to 'deleted'
def delete_unit(db, unit_id: int, schema: DeleteProductUnits):
    unit = db.query(Units).filter(Units.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit.deleted_by = schema.deleted_by
    unit.deletion_date = datetime.now()
    unit.status = settings.STATUS_ENUM[1]  #'deleted' is the second status in the list
    db.commit()
    return "Unit deleted successfully"


# Update an existing product unit
def update_unit(db, unit_id :int, schema: UpdateProductUnits):
    unit = db.query(Units).filter(Units.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")

    unit.name = schema.name
    unit.updated_by = schema.updated_by
    unit.updation_date = datetime.now()
    db.commit()
    db.refresh(unit)    
    return unit
    
