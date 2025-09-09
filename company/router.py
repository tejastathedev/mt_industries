from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .schema import RegisterCompanySchema

from .services import register_company, login, refresh
from fastapi.security import OAuth2PasswordRequestForm
from utils.response import Response


company_router = APIRouter(prefix="/company", tags=["Company Routs"])


@company_router.post("/add_company")
def add_company(payload: RegisterCompanySchema, db: Session = Depends(get_db)):
    company_data = register_company(payload, db)
    return Response.success(data=company_data, message="Company added successfully...")


@company_router.post("/token")
def login_to_get_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    data = login(form_data, db)
    return Response.success(data=data, message="Login Success...")


@company_router.post("/refresh_token")
def refresh_token(token: str, db: Session = Depends(get_db)):
    data = refresh(token, db)

    return Response.success(data=data)

