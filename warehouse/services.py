from .models import Warehouse
from fastapi import HTTPException, status
from config import settings
from datetime import datetime


def insert_warehouse(payload, db, company_id):
    new_warehouse = Warehouse(**payload.dict())  # Correct unpacking
    new_warehouse.company_id=company_id
    db.add(new_warehouse)
    db.commit()
    db.refresh(new_warehouse)  # Populate new values like id
    return new_warehouse


def get_warehouse(id, db):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    return warehouse


def update_warehouse(id, payload, db, company_id):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if not warehouse:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=settings.DATA_NOT_FOUND
        )

    # Update only provided fields
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(warehouse, key, value)
    warehouse.updated_by = company_id
    db.commit()
    db.refresh(warehouse)
    return warehouse


def delete_warehouse(id, db, company_id):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if not warehouse:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=settings.DATA_NOT_FOUND
        )

    warehouse.deleted_by = company_id
    warehouse.deletion_date = datetime.now()
    warehouse.status = settings.STATUS_ENUM[1]
    db.commit()
    db.refresh(warehouse)
    return warehouse
