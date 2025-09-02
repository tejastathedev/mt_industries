from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, func, Float
from products.schema import Constants

from database import Base

class Unit(Base):
    __tablename__='units'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String,nullable=False)
    
    status = Column(Enum('live', 'deleted', name='status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime, default=func.now())


class WeightUnits(Base):
    __tablename__='weight_units'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String,nullable=False)
    
    status = Column(Enum('live', 'deleted', name='status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime, default=func.now())
    company_id=Column(Integer, ForeignKey("companies.id"))


class Categories(Base):
    __tablename__='categories'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String,nullable=False)
    description=Column(String, nullable=False)

    status = Column(Enum('live', 'deleted', name='status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime, default=func.now())
    company_id=Column(Integer, ForeignKey("companies.id"))

class DimensionUnits(Base):
    __tablename__='dimension_units'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String,nullable=False)
    description=Column(String, nullable=False)

    status = Column(Enum('live', 'deleted', name='status_enum'), default=Constants.live)
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    updation_date = Column(DateTime, default=func.now())
    deleted_by = Column(Integer, ForeignKey('users.id'))
    deletion_date = Column(DateTime, default=func.now())
    company_id=Column(Integer, ForeignKey("companies.id"))


class Product(Base):
    __tablename__="products"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String, nullable=False)
    description=Column(Text, nullable=False)
    img=Column(String, nullable=True)
    sku=Column(String, nullable=True)
    weight=Column(Float, nullable=False)
    dimensions=Column(String, nullable=False)
    brand_name=Column(String, nullable=True)
    cost_price=Column(Float, nullable=False)
    market_price=Column(Float, nullable=False)
    selling_price=Column(Float, nullable=False)
    dimension_unit=Column(Integer, ForeignKey("dimension_units.id"))
    category_id=Column(Integer, ForeignKey("categories.id"))
    weight_unit_id=Column(Integer, ForeignKey("weight_units.id"))
    unit_id=Column(Integer,ForeignKey('units.id'))
    initial_stock=Column(Float, nullable=False)
    initial_stock=Column(Float, nullable=False)
