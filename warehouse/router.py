from fastapi import APIRouter, Depends, HTTPException, status
from .schema import WarehouseSchema
from sqlalchemy.orm import Session
from database import get_db
from .services import (
    insert_warehouse,
    get_warehouse,
    update_warehouse,
    delete_warehouse,
)
from auth.tokenEssentials import validate_company_token
from config import settings
from utils.response import Response

warehouse_router = APIRouter(prefix="/warehouse", tags=["Warehouse"])


@warehouse_router.post("/add_warehouse")
def add_warehouse(
    payload: WarehouseSchema,
    db: Session = Depends(get_db),
    company_id: int = Depends(validate_company_token),
):
    new_warehouse = insert_warehouse(payload, db)
    return Response.success(data=new_warehouse)


@warehouse_router.get("/get_warehouse_by_id")
def get_warehouse_by_id(
    id: int,
    db: Session = Depends(get_db),
    company_id: int = Depends(validate_company_token),
):
    if not id:
        raise HTTPException(
            status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,
            detail=settings.DATA_VALIDATION_ERROR,
        )
    warehouse = get_warehouse(id, db)
    if not warehouse:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=settings.DATA_NOT_FOUND
        )
    return Response.success(data=warehouse)


@warehouse_router.put("/update_warehouse_by_id")
def update_warehouse_by_id(
    id: int,
    payload: WarehouseSchema,
    db: Session = Depends(get_db),
    company_id: int = Depends(validate_company_token),
):
    if not id:
        raise HTTPException(
            status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,
            detail=settings.DATA_VALIDATION_ERROR,
        )
    warehouse = update_warehouse(id, payload, db, company_id)
    if not warehouse:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=settings.DATA_NOT_FOUND
        )
    return Response.success(data=warehouse)


@warehouse_router.put("/delete_warehouse_by_id")
def delete_warehouse_by_id(
    id: int,
    db: Session = Depends(get_db),
    company_id: int = Depends(validate_company_token),
):
    if not id:
        raise HTTPException(
            status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,
            detail=settings.DATA_VALIDATION_ERROR,
        )
    warehouse = delete_warehouse(id, db, company_id)
    if not warehouse:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=settings.DATA_NOT_FOUND
        )
    return Response.success(data=warehouse)
