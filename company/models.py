from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    ForeignKey,
    func
)
from database import Base
from sqlalchemy.orm import relationship
from config import settings


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=False)
    password = Column(String, nullable=False)
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
    warehouses = relationship("Warehouse", back_populates="company")
    otp = relationship("CompanyOTP", back_populates='company')