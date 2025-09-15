from database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from config import settings


class OTPQueue(Base):
    __tablename__ = 'otpqueue'
    id = Column(Integer, primary_key=True, autoincrement=True)
    otp_id = Column(Integer, ForeignKey('company_otps.id'))
    otp_creation_date = Column(DateTime, nullable=False)
    
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )

    creation_date = Column(DateTime, default=datetime.now()) 
    # updation_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


    # Relationship
    companyOtp = relationship('CompanyOTP', back_populates='otpQueue', foreign_keys=[otp_id])