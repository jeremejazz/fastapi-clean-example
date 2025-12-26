
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship, MappedAsDataclass, Mapped, mapped_column

from app.infrastructure.database import Base


class CategoryORM(MappedAsDataclass, Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String, unique=True, index=True)
                  

class ProductORM(Base):
    __tablenamne__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Numeric(10, 2, as_decimal=True))
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("CategoryORM", back_populates="products")