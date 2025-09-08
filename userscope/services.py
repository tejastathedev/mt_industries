from sqlalchemy.orm import Session
from fastapi import HTTPException
from userscope.models import UserScope
from sqlalchemy.exc import DatabaseError

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


#deletescopes

def scopesdeletion(id:int,db:Session):
    scopes = db.query(UserScope).filter(UserScope.id == id).first()
    if not scopes:
        raise Exception("Scopes not found")
    db.delete(scopes)
    db.commit()
    return {"message":"deletion completion"}