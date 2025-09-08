from sqlalchemy.orm import Session
from users.models import UserScope, User
from sqlalchemy.exc import DatabaseError
from auth.tokenEssentials import get_pass_hash


def add_object_to_database(object, db: Session):
    db.add(object)
    db.commit()
    return True


def register_scopes(db):
    available_scopes = ["admin", "manager", "staff"]
    for scopes in available_scopes:
        scope = UserScope(scope_name=scopes)
        if not add_object_to_database(scope, db):
            raise DatabaseError("Failed to Add Scopes ", params=None, orig=None)
    return "All the scopes are added !"


def register_user_in_db(input, db):
    user = User(
        first_name=input.first_name,
        last_name=input.last_name,
        phone=input.phone,
        mail=input.mail,
        password=get_pass_hash(input.password),
        scope_id=input.scope_id,
    )
    db.add(user)
    db.commit()
    return "User Created Successfully"
