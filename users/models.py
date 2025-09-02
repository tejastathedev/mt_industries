from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base

class UserScope(Base):
    __tablename__  = 'userscopes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    scope_name = Column(String, nullable=False)

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    mail = Column(String, nullable=False, unique=False)
    company_number = Column(String, nullable=False, unique=True)

    __table_args__ = CheckConstraint(
        "company_number '^[0-9]{10}$'", 
        name="company_phone_check_constraint"
    )

