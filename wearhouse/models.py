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
from config import settings


# 3. Warehouse
# ===========================
class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.id"),nullable=False)
    users_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    warehouse_name = Column(String, nullable=False)
    warehouse_manager = Column(String)
    details = Column(String)

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"),
        default=settings.STATUS_ENUM[0],
    )

    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    # ✅ Relationship
    company = relationship("Company", back_populates="warehouses")
    users = relationship("User",back_populates="warehouses",foreign_keys=[users_id])
