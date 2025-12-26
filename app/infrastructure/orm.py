
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class CategoryORM(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
                  

class ProductORM(Base):
    __tablenamne__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Numeric(10, 2, as_decimal=True))
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("CategoryORM", back_populates="products")