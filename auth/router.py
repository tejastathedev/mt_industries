
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from auth.services import login

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/token')
def login_to_get_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return login(form_data, db)
