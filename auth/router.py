
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from auth.services import login, generateAccessandRefreshToken, removeTokenAtLogout
from auth.schema import TokenSchema
from auth.tokenEssentials import validate_token
auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/token')
def allTokensGeneration(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return login(form_data, db)


@auth_router.post('/generateaccesstoken')
def generateAccessToken(token : TokenSchema, db : Session = Depends(get_db)):
    return generateAccessandRefreshToken(token.token, db)

@auth_router.post('/removetokens')
def removeTokensBeforeLogout(token : str = Depends(validate_token), db : Session = Depends(get_db)):
    return removeTokenAtLogout(token, db)
