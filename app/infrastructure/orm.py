
from decimal import Decimal
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship, mapped_column

from app.infrastructure.database import Base


class CategoryORM(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] = mapped_column(unique=True, index=True)
                  

class ProductORM(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True)
    price:Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2, asdecimal=True))
    # category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    # category: Mapped[CategoryORM] = relationship(back_populates="products")