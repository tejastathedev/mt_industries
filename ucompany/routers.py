from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from ucompany.services import company_creation,company_by_id,company_deletion,company_updation,companies
from . import schema

company_routers = APIRouter(prefix='/company',tags = ['company'])

#compnaycreation
@company_routers.post("/registeration")
def companycreation(company:schema.CompanyCreation,db:Session=Depends(get_db)):
    return company_creation(company,db)

#company show by id
@company_routers.get("/showbyid")
def companybyid(email:str,password:str,db:Session=Depends(get_db)):
    return company_by_id(email,password,db)

#company updation 
@company_routers.put("/updation")
def companyupda(email:str,password:str,company:schema.Companyupdation,db:Session=Depends(get_db)):
    return company_updation(email,password,company,db)

#compnay deletion
@company_routers.delete("/deletion")
def companydeletion(email:str,password:str,db:Session=Depends(get_db)):
    return company_deletion(email,password,db)

#all companies 
@company_routers.get("/allcompanies")
def all_companies(db:Session=Depends(get_db)):
    return companies(db)