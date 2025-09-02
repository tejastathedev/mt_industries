from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, DateTime, func, Enum
from sqlalchemy.orm import relationship
from database import Base
from users.schema import Constants
from orders.models import Order

class UserScope(Base):
    __tablename__  = 'userscopes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    scope_name = Column(String, nullable=False)
    users = relationship('User', back_populates='scopes')
 
class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    mail = Column(String, nullable=False, unique=False)
    phone = Column(String, nullable=False, unique=True)
    status = Column(Enum('live', 'deleted', name='status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime, default=func.now())

    users = relationship('User', back_populates='company')
    created_by_user = relationship('User', foreign_keys=[created_by])
    updated_by_user = relationship('User', foreign_keys=[updated_by])
    deleted_by_user = relationship('User', foreign_keys=[deleted_by])



    __table_args__ = CheckConstraint(
        "length(phone) = 10 AND phone GLOB '[0-9]*'", 
        name="company_phone_check_constraint"
    )
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False, unique=True)
    mail = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    access_token = Column(String(32))
    refresh_token = Column(String(32))
    scope_id = Column(Integer, ForeignKey('userscopes.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    otp = Column(Integer)
    status = Column(Enum('live', 'deleted', name='user_status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime)

    scope = relationship('UserScope', back_populates='users', uselist=False)
    company = relationship('Company', back_populates='users', uselist=False)

    created_by_user = relationship('User', remote_side=[id], foreign_keys=[created_by], post_update=True)
    updated_by_user = relationship('User', remote_side=[id], foreign_keys=[updated_by], post_update=True)
    deleted_by_user = relationship('User', remote_side=[id], foreign_keys=[deleted_by], post_update=True)

    created_orders = relationship('Order', foreign_keys=[Order.created_by], back_populates='created_by_user')
    updated_orders = relationship('Order', foreign_keys=[Order.updated_by], back_populates='updated_by_user')
    deleted_orders = relationship('Order', foreign_keys=[Order.deleted_by], back_populates='deleted_by_user')

    __table_args__ = (
        CheckConstraint("length(phone) = 10 AND phone GLOB '[0-9]*'", name="user_phone_check_constraint"),
    )
