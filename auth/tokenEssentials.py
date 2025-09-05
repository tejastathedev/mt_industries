# from jose import jwt, JWTError
from jose import JWTError, jwt
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional
from config import settings
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from users.models import User
from company.models import Company
from database import get_db

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
Oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Creating basic schema to store token and its details
#  which are needed to be accessed later in the authentication process

class Token(BaseModel):
    access_token : str
    token_type : str = "Bearer"
    expires_in : int 

class TokenWithRefresh(Token):
    refresh_token : str

class TokenData(BaseModel):
    mail : Optional[str] = None

# Defining utility functions for password hashing and verifying

def verify_pass(plain_pass : str, hashed_pass : str)-> bool:
    return pwd_context.verify(plain_pass, hashed_pass)

def get_pass_hash(plain_pass : str) -> str:
    return pwd_context.hash(plain_pass)


# Defining functions to do Database operations needed for JWT
def get_user(mail : str, db : Session):
    user = db.query(User).filter(User.mail == mail).first()
    return user if user else None

def authenticate_user_pass(mail : str, password : str, db : Session):
    user = get_user(mail, db)
    if not user:
        return False
    hashed_pass = user.password
    if not verify_pass(password, hashed_pass):
        return False
    
    if user.status != settings.STATUS_ENUM[0]:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"User is {user.status}")
    return user

# Defining functions to do Database operations needed for JWT
def get_company(mail : str, db : Session):
    company = db.query(Company).filter(Company.email == mail).first()
    return company if company else None

def authenticate_company_pass(mail : str, password : str, db : Session):
    company = get_company(mail, db)
    if not company:
        return False
    hashed_pass = company.password
    if not verify_pass(password, hashed_pass):
        return False
    
    if company.status != settings.STATUS_ENUM[0]:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"User is {company.status}")
    return company


# Access Token Creation Function
def create_access_token(subject : str, db : Session) -> str:
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode = {
        "sub" : subject,
        "iat" : int(datetime.now(timezone.utc).timestamp()),
        "exp" : int(expire.timestamp())
    }
    encoded = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    # Storing access token in database
    db.query(User).filter(User.mail == subject).update({"access_token" : encoded})
    db.commit()

    return encoded

def create_refresh_token(subject : str, db : Session) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {
        "sub" : subject,
        "iat" : int(datetime.now(timezone.utc).timestamp()),
        "exp" : int(expire.timestamp())
    }
    encoded = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    db.query(User).filter(User.mail == subject).update({"refresh_token" : encoded})
    db.commit()
    return encoded

def decode_token(token:str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError :
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Could not validate token",
            headers={"WWW-Authenticate" : "Bearer"}
        )

def validate_token(token : str = Depends(Oauth2Scheme), db : Session = Depends(get_db))->str:
    credential_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Could not validate token",
            headers={"WWW-Authenticate" : "Bearer"}
        )
    try:
        # check in database if the token is present?
        user = db.query(User).filter(User.access_token == token).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unAuthenticated")
        print("validation has hit")
        payload = decode_token(token)
        user_mail : str = payload.get("sub")
        if user_mail is None:
            raise credential_error
        token_data = TokenData(mail=user_mail)
    except JWTError:
        return credential_error

    user_in_db = get_user(token_data.mail, db)   
    if user_in_db is None or user_in_db.status != settings.STATUS_ENUM[0]:
        raise credential_error
    return token



