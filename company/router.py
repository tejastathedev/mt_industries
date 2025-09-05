from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .schema import RegisterCompanySchema
from .services import register_company, login, get_companies
from auth.tokenEssentials import validate_token
from fastapi.security import OAuth2PasswordRequestForm


company_router = APIRouter(prefix="/company", tags=["Company Routs"])


@company_router.post("/add_company")
def add_company(payload: RegisterCompanySchema, db: Session = Depends(get_db)):
    company_data = register_company(payload, db)
    return {"data": company_data}

@company_router.post('/token')
def login_to_get_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return login(form_data, db)


@company_router.get("/get_all_companies")
def get_all_companies(db:Session =Depends(get_db), token:bool=Depends(validate_token)):
    return get_companies(db)
