from typing import Optional
from pydantic import BaseModel
from sqlalchemy.exc import DatabaseError, IntegrityError
from config import settings
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from users.auth import authenticate_user_pass, create_access_token, create_refresh_token, TokenWithRefresh, get_pass_hash
from users.models import UserScope, User, Company
auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/token')
def login_to_get_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = authenticate_user_pass(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Login Credentials")
    # update access and refresh token in database
    access_token = create_access_token(form_data.username, db)
    refresh_token = create_refresh_token(form_data.username, db)

    return TokenWithRefresh(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60,
        refresh_token=refresh_token
    )


@auth_router.post('/dummmyscoperegister')
def register_dummy_scope(db : Session = Depends(get_db)):
    try:
        scope = UserScope(id = 1, scope_name = "Admin")
        db.add(scope)
        db.commit()
        return "Scope Added"
    except DatabaseError as de:
        print(de)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


# id = Column(Integer, primary_key=True, autoincrement=True)
# first_name = Column(String(100), nullable=False)
# last_name = Column(String(100), nullable=False)
# phone = Column(String(15), nullable=False, unique=True)
# mail = Column(String(255), unique=True, nullable=False)
# password = Column(String(255), nullable=False)
# access_token = Column(String(32))
# refresh_token = Column(String(32))
# scope_id = Column(Integer, ForeignKey("userscopes.id"))
# company_id = Column(Integer, ForeignKey("companies.id"))
# otp = Column(Integer)
# status = Column(
#     Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
# )
# creation_date = Column(DateTime, default=func.now())
# created_by = Column(Integer, ForeignKey("users.id"))
# updated_by = Column(Integer, ForeignKey("users.id"))
# updation_date = Column(DateTime, default=func.now(), onupdate=func.now())
# deleted_by = Column(Integer, ForeignKey("users.id"))
# deletion_date = Column(DateTime)

class RegisterSchema(BaseModel):
    first_name : str
    last_name : str
    phone : str
    mail : str
    password : str
    scope_id : int

# name = Column(String, nullable=False, unique=True)
# mail = Column(String, nullable=False, unique=False)
# phone = Column(String, nullable=False, unique=True)
# status = Column(
#     Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
# )
# creation_date = Column(DateTime, default=func.now())
# created_by = Column(Integer, ForeignKey("users.id"))
# updated_by = Column(Integer, ForeignKey("users.id"))
# updation_date = Column(DateTime, default=func.now())
# deleted_by = Column(Integer, ForeignKey("users.id"))
# deletion_date = Column(DateTime)
    
@auth_router.post('/dummmyregister')
def register_dummy(input : RegisterSchema, db : Session = Depends(get_db)):
    try:
        user = User(
            first_name = input.first_name, last_name = input.last_name,
            phone = input.phone, mail = input.mail, password = get_pass_hash(input.password), scope_id = input.scope_id,
                    )
        db.add(user)
        db.commit()
        return "User Created Successfully"
    except IntegrityError as ie:
        print(ie)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="There is a user with same registered mobile number or email !")
    except DatabaseError as de:
        print(de)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")