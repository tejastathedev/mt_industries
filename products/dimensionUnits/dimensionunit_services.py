from fastapi import HTTPException
from ..models import DimensionUnits
from ..dimensionUnits.dimensionunit_schema import CreateDimensionUnits, UpdateDimensionUnits, DeleteDimensionUnits, DimensionUnitsResponse
from datetime import datetime
from config import settings
from datetime import datetime

# Service functions for product dimension units
# Create a new product dimension unit
def create_dimensionunit(db, schema: CreateDimensionUnits):
    # Check if a dimension unit with the same name already exists and is not deleted
    existing_dimensionunit = db.query(DimensionUnits).filter(
        DimensionUnits.name == schema.name
    ).first()

    # If it exists, raise an HTTP 400 error
    if existing_dimensionunit:
        raise HTTPException(
            status_code=400,
            detail="Dimension Unit with this name already exists."
        )
    # If it doesn't exist, create a new dimension unit
    new_dimensionunit = DimensionUnits(
        name=schema.name,
        description=schema.description,
        created_by=schema.created_by,
        company_id=schema.company_id,
        status=settings.STATUS_ENUM[0],  # 'active' is the first status in the list
        creation_date=datetime.now(),
    )

    db.add(new_dimensionunit)
    db.commit()
    db.refresh(new_dimensionunit)  # ← necessary to get the auto-generated ID

    return new_dimensionunit  # This matches response_model=DimensionUnitResponse

# Retrieve all product dimension units
def get_dimensionunits(db):
    dimensionunits=db.query(DimensionUnits).filter(DimensionUnits.status != settings.STATUS_ENUM[1]).all()  # Exclude 'deleted' dimension units
    if not dimensionunits:
        return []
    return dimensionunits

# Soft delete a product dimension unit by updating its status to 'deleted'
def delete_dimensionunit(db, dimensionunit_id: int, schema: DeleteDimensionUnits):
    dimensionunit = db.query(DimensionUnits).filter(DimensionUnits.id == dimensionunit_id).first()
    if not dimensionunit:
        raise HTTPException(status_code=404, detail="Dimension Unit not found")
    dimensionunit.deleted_by = schema.deleted_by
    dimensionunit.deletion_date = datetime.now()
    dimensionunit.status = settings.STATUS_ENUM[1]  #'deleted' is the second status in the list
    db.commit()
    return "Dimension Unit deleted successfully"


# Update an existing product dimension unit
def update_dimensionunit(db, dimensionunit_id :int, schema: UpdateDimensionUnits):
    dimensionunit = db.query(DimensionUnits).filter(DimensionUnits.id == dimensionunit_id).first()
    if not dimensionunit:
        raise HTTPException(status_code=404, detail="Dimension Unit not found")

    # Check if a dimension unit with the new name already exists and is not deleted
    existing_dimensionunit = db.query(DimensionUnits).filter(
        DimensionUnits.name == schema.name,
        DimensionUnits.id != dimensionunit_id,  # Exclude the current dimension unit
        DimensionUnits.status != settings.STATUS_ENUM[1]  # Exclude 'deleted' dimension units
    ).first()

    if existing_dimensionunit:
        raise HTTPException(
            status_code=400,
            detail="Dimension Unit with this name already exists."
        )

    dimensionunit.name = schema.name
    dimensionunit.description = schema.description
    dimensionunit.updated_by = schema.updated_by
    dimensionunit.updation_date = datetime.now()
    db.commit()
    db.refresh(dimensionunit)  # ← to get the updated data

    return dimensionunit  # This matches response_model=DimensionUnitResponse

