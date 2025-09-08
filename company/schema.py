from pydantic import BaseModel


class RegisterCompanySchema(BaseModel):
    name:str
    phone:str
    email:str
    password:str