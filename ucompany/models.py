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


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    mail = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    password = Column(String,nullable=False)
    

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"),
        default=settings.STATUS_ENUM[0],
    )

    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    # Relationships
    users = relationship("User", back_populates="company",foreign_keys="[User.company_id]")# foreign_keys=[User.company_id]
    warehouses = relationship("Warehouse", back_populates="company")

    __table_args__ = (
        CheckConstraint(
            "length(phone) = 10 AND phone GLOB '[0-9]*'",
            name="company_phone_check_constraint",
        ),
    )

