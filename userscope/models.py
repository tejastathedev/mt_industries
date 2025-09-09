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


# ===========================
# 1. UserScope
# ===========================
class UserScope(Base):
    __tablename__ = "userscopes"

    id = Column(Integer, primary_key=True,autoincrement=True)
    scope_name = Column(String, nullable=False, unique=True)

    # Relationships
    users = relationship("User", back_populates="scopes")