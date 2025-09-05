
from fastapi import status, HTTPException
from config import settings
from .models import Company
from auth.tokenEssentials import (
    authenticate_company_pass,
    create_access_token,
    create_refresh_token,
    TokenWithRefresh,
)
from auth.tokenEssentials import get_pass_hash


def login(form_data, db):
    # Authenticate the user with thier credentials
    user = authenticate_company_pass(form_data.username, form_data.password, db)
    # Raising an error if the user has incorrect credentials
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Login Credentials")
    
    # update access and refresh token in database
    access_token = create_access_token(form_data.username, db)
    refresh_token = create_refresh_token(form_data.username, db)

    # Returning the refresh and access token
    return TokenWithRefresh(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60,
        refresh_token=refresh_token
    )


def register_company(payload, db):
    company = Company(
        name=payload.name,
        phone=payload.phone,
        email=payload.email,
        password=get_pass_hash(payload.password),
    )
    db.add(company)
    db.commit()
    return "Company added successfully...!"

def get_companies(db):
    companies=db.query(Company).all()
    return companies

