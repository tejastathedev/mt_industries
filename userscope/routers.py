from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .services import register_scopes,showscopes,scopesdeletion

userscope_router = APIRouter(prefix='/userscope', tags=['userscope'])

#company Creation

@userscope_router.post("/creation")
def userscope_creation(db:Session=Depends(get_db)):
    return register_scopes(db)

@userscope_router.get("/showscopes")
def show_user_scopes(db:Session=Depends(get_db)):
    return showscopes(db)


@userscope_router.delete("/deletion")
def user_scopes_deletion(id:int,db:Session=Depends(get_db)):
    return scopesdeletion(id,db)