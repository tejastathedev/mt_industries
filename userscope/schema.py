from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from config import settings

#schemas for UserScope

class UserScope(BaseModel):
    scope_name: str

class ScopeResponse():
    id:int

    class Config:
        orm_mode = True
