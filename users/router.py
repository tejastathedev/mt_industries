from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from users.services import register_scopes, register_user_in_db
from users.schema import RegisterSchema



user_router = APIRouter(prefix='/user', tags=['user'])



@user_router.post('/pushAllScopes')
def register_all_scopes(db : Session = Depends(get_db)):
    return register_scopes(db)



@user_router.post('/register')
def register_user(input : RegisterSchema, db : Session = Depends(get_db)):
    return register_user_in_db(input, db)
# Changed comment