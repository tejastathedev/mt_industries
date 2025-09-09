from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from wearhouse.services import warehouse_by_id,warehouse_deletion,Warehouse_creation,warehouses,Warehouse_updation
from . import schema

wearhouse_router = APIRouter(prefix='/Wearhouse', tags=['Wearhouse'])


@wearhouse_router.post("/Registration")
def wearcreation(wearhouse:schema.WarehouseCreate,db:Session=Depends(get_db)):
    return Warehouse_creation(wearhouse,db)

@wearhouse_router.put("/updation")
def wearupdation(id:int,wearhouse:schema.WarehouseUpdation,db:Session=Depends(get_db)):
    return Warehouse_updation(id,wearhouse,db)

@wearhouse_router.delete("/deletion")
def weardeletion(id:int,wearhouse:schema.Warehousedeletion,db:Session=Depends(get_db)):
    return warehouse_deletion(id,wearhouse,db)

@wearhouse_router.get("/get_by_id")
def wearbyid(id:int,db:Session=Depends(get_db)):
    return warehouse_by_id(id,db)

@wearhouse_router.get("/all_warehouse")
def warehouse_all(db:Session=Depends(get_db)):
    return warehouses(db)
