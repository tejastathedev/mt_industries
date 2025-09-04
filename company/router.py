from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .schema import RegisterCompanySchema
from .services import register_company

company_router = APIRouter(prefix="/company", tags=["Company Routs"])


@company_router.post("add_company")
def add_company(payload: RegisterCompanySchema, db: Session = Depends(get_db)):
    company_data = register_company(payload, db)
    return {"data": company_data}
