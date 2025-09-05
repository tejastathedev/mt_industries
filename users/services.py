from sqlalchemy.orm import Session
from users.models import UserScope, User
from sqlalchemy.exc import DatabaseError
from auth.tokenEssentials import get_pass_hash,verify_pass
from passlib.context import CryptContext
from .models import User, UserScope
from . import schema

#this function for reusable we dont need to write commit
def add_object_to_database(obj, db: Session):
    try:
        db.add(obj)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"Error adding object: {e}")
        return False

#registerscopes 
def register_scopes(db: Session):
    predefined_scopes = [
        {"id": 1, "scope_name": "Admin"},
        {"id": 2, "scope_name": "Manager"},
        {"id": 3, "scope_name": "Staff"},
    ]
    for scope in predefined_scopes:
        existing = db.query(UserScope).filter_by(id=scope["id"]).first()
        if not existing:
            user_scope = UserScope(id=scope["id"], scope_name=scope["scope_name"])
            if not add_object_to_database(user_scope, db):
                raise Exception(f"Failed to add scope {scope['scope_name']}")

    return "All the scopes are added!"


#scopesResponse
def showscopes(db:Session):
    scopes = db.query(UserScope).all()
    return {"scopes":scopes}


# registerUser
def register_users(user:schema.UserCreate, db:Session):
    existing_user = db.query(User).filter_by(mail=user.mail).first()
    if existing_user:
        raise ValueError("User with this email already exists.")
    hashed_pw = get_pass_hash(user.password)

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        scope_id=user.scope_id,
        company_id=user.company_id,
        status = user.status,
        mail=user.mail,
        password=hashed_pw,
        created_by=user.created_by,
        creation_date = user.creation_date
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message":"The user register successfully"}

def get_user_info(email: str, password: str, db: Session):
    user = db.query(User).filter(User.mail == email).first()
    if not user or not verify_pass(password, user.password):
        raise Exception("Invalid credentials")
    return {"message":"Login successfully"}

#update User details
def update_user(email: str, password: str, update:schema.UserUpdate, db: Session):
    user = db.query(User).filter(User.mail == email).first()
    if not user or not verify_pass(password, user.password):
        raise Exception("Invalid credentials")
    user.first_name=update.first_name
    user.last_name=update.last_name
    user.phone=update.phone
    user.scope_id=update.scope_id
    user.company_id=update.company_id
    user.status=update.status
    user.updated_by = update.updated_by
    user.updation_date=update.updation_date
    user.password = get_pass_hash(update.password)
    db.commit()
    db.refresh(user)
    return {"message":"The Profile update successfully"}

#deletion User Details
def delete_user(email:str,password:str, db:Session):
    user = db.query(User).filter(User.email==email).first()
    if not user or not verify_pass(password,user.password):
        raise Exception("Invalid credential")
    db.delete(user)
    db.commit()
    return {"message":"User Delete Successfully"}