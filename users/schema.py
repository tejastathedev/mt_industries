from pydantic import BaseModel


class RegisterSchema(BaseModel):
    first_name : str
    last_name : str
    phone : str
    mail : str
    password : str
    scope_id : int
