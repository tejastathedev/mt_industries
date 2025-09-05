from database import Base
from sqlalchemy import Column, Enum, Integer, String, ForeignKey, DateTime, func
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from config import settings

class CompanyOTP(Base):
    __tablename__ = 'company_otps'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    otp = Column(String, nullable=False)
    
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )

    hits = Column(Integer, default=0)
    generationHits = Column(Integer, default=0)

    creation_date = Column(DateTime, default=func.now())
    updation_date = Column(DateTime, default=func.now(), onupdate=func.now())


    # Relationship
    company = relationship('Company', back_populates='otp', foreign_keys=[company_id])