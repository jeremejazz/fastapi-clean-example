
from typing import List, Optional
from sqlalchemy.orm import Session

from app.domain.interfaces import CategoryRepository, ProductRepository
from app.domain.models import Product, Category
from app.infrastructure.orm import ProductORM, CategoryORM

class SQLAlchemyCategoryRepository(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, category: Category):

        category_search = self.get_by_name(category.name)
        if category_search:
            raise ValueError(f"Category with name `{category.name}` already exists")

        category_orm = CategoryORM(name=category.name)
        self.db.add(category_orm)
        self.db.commit()

        return Category(id=category_orm.id, name=category_orm.name)
    

    def get_by_id(self, category_id: int) -> Optional[Category]:
        category_orm = self.db.query(CategoryORM).filter(CategoryORM.id == category_id).first()
        if category_orm:
            return Category(id=category_orm.id, name=category_orm.name)
        return None

    def get_by_name(self, name):
        return self.db.query(CategoryORM).filter(CategoryORM.name == name).first()

    def list_all(self):
        orms = self.db.query(CategoryORM).all()
        return [Category(id=x.id, name=x.name) for x in orms]
          
        
    

class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product) -> Product:
            product_orm = ProductORM(
                name=product.name, 
                price=product.price, 
                category_id=product.category_id
            )
            self.db.add(product_orm)
            self.db.commit()
            self.db.refresh(product_orm)
            return Product(
                id=product_orm.id, 
                name=product_orm.name, 
                price=product_orm.price, 
                category_id=product_orm.category_id
            )

    def get_by_id(self, product_id: int) -> Optional[Product]:
        product_orm: Optional[ProductORM] = self.db.query(ProductORM).filter(ProductORM.id == product_id).first()
        if product_orm:
            return Product(id=product_orm.id, name=product_orm.name, price=product_orm.price, category_id=product_orm.category_id)
        return None

    def list_all(self) -> List[Product]:
        orms = self.db.query(ProductORM).all()
        return [
            Product(id=p.id, name=p.name, price=p.price, category_id=p.category_id) 
            for p in orms
        ]