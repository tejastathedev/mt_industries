from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
    Enum,
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


# TODO: add email check constraint for emails !

# Warehouse table schema docs:
# id -> pk, autoincrement
# company_id : relationship with companies.id
# location parameter: latitude , longitude, address
# warehouse related columns: warehouse_name, warehouse_manager, details





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
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))

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
    warehouse = relationship("Warehouse", back_populates="users", uselist=False, foreign_keys=[warehouse_id])
    
