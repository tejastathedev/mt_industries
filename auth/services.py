# from fastapi import status, HTTPException
# from config import settings
# from auth.tokenEssentials import authenticate_user_pass, create_access_token, create_refresh_token, TokenWithRefresh

# def login(form_data, db):
#     # Authenticate the user with thier credentials
#     user = authenticate_user_pass(form_data.username, form_data.password, db)
#     # Raising an error if the user has incorrect credentials
#     if not user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Login Credentials")
    
#     # update access and refresh token in database
#     access_token = create_access_token(form_data.username, db)
#     refresh_token = create_refresh_token(form_data.username, db)

#     # Returning the refresh and access token
#     return TokenWithRefresh(
#         access_token=access_token,
#         token_type="bearer",
#         expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60,
#         refresh_token=refresh_token
#     )