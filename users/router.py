from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from users.services import register_scopes,register_users,update_user,get_user_info,delete_user,showscopes
from . import schema

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/pushAllScopes')
def register_all_scopes(db : Session = Depends(get_db)):
    return register_scopes(db)

@user_router.get('/showscopes')
def show_scopes(db:Session=Depends(get_db)):
    return showscopes(db)

@user_router.post('/registerUsers')
def register_of_users(user:schema.UserCreate, db:Session=Depends(get_db)):
    return register_users(user,db)

@user_router.get('/showuserinfo')
def showuser(email:str,password:str,db:Session=Depends(get_db)):
    return get_user_info(email,password,db)

@user_router.put('/Userupdation')
def user_updation(email:str,password:str,update:schema.UserUpdate, db: Session=Depends(get_db)):
    return update_user(email,password,update,db)

@user_router.delete('/Userdeletion')
def user_deletion(email:str,password:str,db : Session = Depends(get_db)):
    return delete_user(email,password, db)
