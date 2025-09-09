from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import DatabaseError
from auth.tokenEssentials import get_pass_hash,verify_pass
from passlib.context import CryptContext
from .models import Company
from . import schema


#creation company

def company_creation(company:schema.CompanyCreation,db:Session):
    existingcompany = db.query(Company).filter(Company.mail==company.mail).first()
    if existingcompany:
        raise Exception("The company already exist")
    new_company = Company(
        name = company.name,
        mail= company.mail,
        phone=company.phone,
        status=company.status,
        password = get_pass_hash(company.password),
        created_by = company.created_by,
        creation_date =company.creation_date
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return {"message":"The Comapnay Created Successfully"}

#updation company

def company_updation(email:str,password:str,company:schema.Companyupdation,db:Session):
    company1 = db.query(Company).filter(Company.mail==email).first()
    if not company1 or not verify_pass(password,company1.password):
        raise HTTPException("The credetials are wrong")
    
    company1.name = company.name
    company1.phone = company.phone
    company1.password = get_pass_hash(company.password)
    company1.status =company.status
    company1.updated_by = company.updated_by
    company1.updation_date = company.updation_date
    company1.mail == company.mail

    db.commit()
    db.refresh(company1)
    return {"message":"The company Updation done"}


#deletion company

def company_deletion(email:str,password:str,db:Session):
    company = db.query(Company).filter(Company.mail==email).first()
    if not company or not verify_pass(password,company.password):
        raise HTTPException("The credetials are wrong")
    db.delete(company)
    db.commit()

    return {"message":"The company deletion done"}


#show companies by their identity
def company_by_id(email:str,password:str,db:Session):
    company = db.query(Company).filter(Company.mail==email).first()
    if not company or not verify_pass(password, company.password):
        raise HTTPException("The company not exists")
    return company

# show all companies
def companies(db:Session):
    companies = db.query(Company).all()
    return companies
