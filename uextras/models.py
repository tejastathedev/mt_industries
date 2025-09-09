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
from datetime import datetime


class OTP(Base):
    __tablename__ = 'otps'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Integer)
    otp_code = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    expired_at = Column(DateTime, default=datetime.now())
    creation_date = Column(DateTime, default=datetime.now())
    generationHits = Column(Integer, default=0)
    
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    
