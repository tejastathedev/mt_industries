from sqlalchemy import Column, Integer, ForeignKey, Float, String, Enum, DateTime, func
from sqlalchemy.orm import relationship
from config import settings
from database import Base
from datetime import datetime

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
    creation_date = Column(DateTime, default=datetime.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=datetime.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    # Relationships

    company = relationship("Company", back_populates="warehouses")
    users = relationship("User", back_populates="warehouse", foreign_keys="[User.warehouse_id]")

