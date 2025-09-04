from sqlalchemy.exc import DatabaseError
from config import settings
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from users.auth import authenticate_user_pass, create_access_token, create_refresh_token, TokenWithRefresh
from users.models import UserScope
auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/token')
def login_to_get_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = authenticate_user_pass(form_data.username, form_data.password)
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
    except DatabaseError as de:
        print(de)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


# @auth_router.post('/dummmyregister')
# def register_dummy(db : Session = Depends(get_db)):
#     try:
#         scope = UserScope(id = 1, ) 
