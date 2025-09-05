from fastapi import status, HTTPException
from config import settings
from auth.tokenEssentials import create_access_token, create_refresh_token
from auth.tokenEssentials import Token, validate_token, decode_token, authenticate_user_pass
from sqlalchemy.orm import Session
from users.models import User

def login(form_data, db):
    # Authenticate the user with thier credentials
    user = authenticate_user_pass(form_data.username, form_data.password, db)
    # Raising an error if the user has incorrect credentials
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Login Credentials")
    
    # update access and refresh token in database
    access_token = create_access_token(form_data.username, db)
    create_refresh_token(form_data.username, db)

    # Returning the access token to the user
    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60
    )

def generateAccessandRefreshToken(token : str, db):
    # Is this access token present in the database?
    user = db.query(User).filter(User.access_token == token).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Access Token might be Expired")
    
    # Validate the token
    is_token_valid = validate_token(token, db)

    # return exception if not validated
    if not is_token_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unauthorized")

    # Decode the user_mail from the access token
    payload = decode_token(token)

    # Create a new access token and refresh token and make registry to database
    accessToken = create_access_token(payload.get("sub"), db)

    # Return Access Token
    return Token(
        access_token=accessToken,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60
    )


def removeTokenAtLogout(token, db : Session):
    # Validate the token
    isTokenValid = validate_token(token, db)
    print(isTokenValid)
    # return exception if not validated
    if not isTokenValid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="UnAuthorized")

    payload = decode_token(token).get("sub")
    print("user_mail: ", payload)

    # Remove the access and refresh token from the database
    query_result = db.query(User).filter(User.mail == payload).update({"access_token" : "", "refresh_token" : ""})
    db.commit()
    print(query_result)
    # if not query_result:
    #     raise HTTPException("No Tokens Present !")
    return "Tokens removed, Logout can be processed further"