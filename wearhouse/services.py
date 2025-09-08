from sqlalchemy.orm import Session
from fastapi import HTTPException
from wearhouse.models import Warehouse
from sqlalchemy.exc import DatabaseError
from auth.tokenEssentials import get_pass_hash,verify_pass
from passlib.context import CryptContext
from . import schema
from config import settings


def Warehouse_creation(warehouse:schema.WarehouseCreate,db:Session):
    # existingwearhouse = db.query(Warehouse).filter(Warehouse.id == warehouse.id).first()
    # if existingwearhouse:
    #     raise Exception("the wearhouse already exist")
    new_Warehouse = Warehouse(
        company_id = warehouse.company_id,
        user_id = warehouse.user_id,
        warehouse_name = warehouse.warehouse_name,
        warehouse_manager= warehouse.warehouse_manager,
        latitude = warehouse.latitude,
        longitude = warehouse.longitude,
        address = warehouse.address,
        details = warehouse.details,
        creation_date = warehouse.creation_date
    )
    db.add(new_Warehouse)
    db.commit()
    db.refresh(new_Warehouse)

    return {"message":"The wearhouse r0gister successfully"}

def Warehouse_updation(id:int,warehouse1:schema.WarehouseUpdation,db:Session):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if not warehouse:
        raise Exception("The warehouse not exist")
    warehouse.warehouse_name==warehouse1.warehouse_name
    warehouse.warehouse_manager = warehouse1.warehouse_manager
    warehouse.company_id = warehouse1.company_id
    warehouse.user_id = warehouse1.user_id
    warehouse.address = warehouse1.address
    warehouse.latitude = warehouse1.latitude
    warehouse.longitude = warehouse.longitude
    warehouse.details = warehouse.details
    warehouse.status = warehouse.status
    warehouse.updated_by = warehouse.updated_by
    warehouse.updation_date = warehouse.updation_date
    db.commit()
    db.refresh(warehouse)
    return {"message":"The updation has done"}

def warehouse_deletion(id:int,wear:schema.Warehousedeletion,db:Session):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if not warehouse:
        raise Exception("The warehouse not exists")
    warehouse.deleted_by = wear.deleted_by
    warehouse.deletion_date = wear.deletion_date

    db.delete(warehouse)
    db.commit()
    return {"message":"The deletion done successfully"}


def warehouse_by_id(id:int,db:Session):
    warehouse = db.query(Warehouse).filter(Warehouse.id==id).first()
    if not warehouse:
        raise Exception("The warehouse not exists")
    return warehouse


#show all wearhouses
def warehouses(db:Session):
    warehouse = db.query(Warehouse).all()
    return warehouse
