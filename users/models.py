from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    CheckConstraint,
    DateTime,
    func,
    Enum,
    Float,
)
from sqlalchemy.orm import relationship
from database import Base
from orders.models import Order
from config import settings


class UserScope(Base):
    __tablename__ = "userscopes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    scope_name = Column(String, nullable=False, unique=True)

    # Relationships
    users = relationship("User", back_populates="scopes")


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    mail = Column(String, nullable=False, unique=False)
    phone = Column(String, nullable=False, unique=True)
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)


    # Relationships
    users = relationship("User", back_populates="company", foreign_keys="[User.company_id]")
    warehouses = relationship("Warehouse", back_populates="company")

    __table_args__ = (
        CheckConstraint(
            "length(phone) = 10 AND phone GLOB '[0-9]*'",
            name="company_phone_check_constraint",
        ),
    )
    # TODO: add email check constraint for emails !

# Warehouse table schema docs:
# id -> pk, autoincrement
# company_id : relationship with companies.id
# location parameter: latitude , longitude, address
# warehouse related columns: warehouse_name, warehouse_manager, details


class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    warehouse_name = Column(String, nullable=False)
    warehouse_manager = Column(String)
    details = Column(String)
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    # Relationships

    company = relationship("Company", back_populates="warehouses")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    mail = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    access_token = Column(String(32))
    refresh_token = Column(String(32))
    scope_id = Column(Integer, ForeignKey("userscopes.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    otp = Column(Integer)
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    # Relationships
    scopes = relationship("UserScope", back_populates="users", uselist=False)
    company = relationship("Company", back_populates="users", uselist=False, foreign_keys=[company_id])

    __table_args__ = (
        CheckConstraint(
            "length(phone) = 10 AND phone GLOB '[0-9]*'",
            name="user_phone_check_constraint",
        ),
    )
    # TODO: add email check constraint for emails !
