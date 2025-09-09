from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Enum,
    DateTime,
    ForeignKey,
    func,
    Float,
)
from sqlalchemy.orm import relationship
from database import Base
from config import settings
from company.models import Company
# from orders.models import OrderProduct


class Units(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    products = relationship("Products", back_populates="units")


class WeightUnits(Base):
    __tablename__ = "weight_units"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

    products = relationship("Products", back_populates="weight_units")


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

    products = relationship("Products", back_populates="categories")


class DimensionUnits(Base):
    __tablename__ = "dimension_units"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

    products = relationship("Products", back_populates="dimension_units")


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    img = Column(String, nullable=True)
    sku = Column(String, nullable=True)
    weight = Column(Float, nullable=False)
    dimensions = Column(String, nullable=False)
    brand_name = Column(String, nullable=True)
    cost_price = Column(Float, nullable=False)
    market_price = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)
    dimension_unit_id = Column(Integer, ForeignKey("dimension_units.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    weight_unit_id = Column(Integer, ForeignKey("weight_units.id"))
    unit_id = Column(Integer, ForeignKey("units.id"))
    initial_stock = Column(Float, nullable=False)
    initial_stock = Column(Float, nullable=False)

    dimension_units = relationship("DimensionUnits", back_populates="products")
    categories = relationship("Categories", back_populates="products")
    weight_units = relationship("WeightUnits", back_populates="products")
    units = relationship("Units", back_populates="products")
    product_stock_history = relationship(
        "ProductStockHistory", back_populates="products"
    )
    order_products = relationship("OrderProduct", back_populates="product")

    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))


class ProductStockHistory(Base):
    __tablename__ = "product_stock_history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    stock_type = Column(
        Enum("stock", "opening", "sale", name="stock_type_enum"),
        default=settings.STATUS_ENUM[0],
    )
    stock = Column(Float, nullable=False)
    prev_stock = Column(Float, nullable=False)
    current_stock = Column(Float, nullable=False)
    status = Column(
        Enum(*settings.STATUS_ENUM, name="status_enum"), default=settings.STATUS_ENUM[0]
    )
    creation_date = Column(DateTime, default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    updation_date = Column(DateTime, onupdate=func.now())
    deleted_by = Column(Integer, ForeignKey("users.id"))
    deletion_date = Column(DateTime)

    products = relationship("Products", back_populates="product_stock_history")

