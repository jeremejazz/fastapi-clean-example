

from decimal import Decimal
from typing import List
from app.domain.interfaces import CategoryRepository, ProductRepository
from app.domain.models import Product


class ProductService:
    def __init__(self, product_repo: ProductRepository, category_repo: CategoryRepository):
        self.product_repo = product_repo
        self.category_repo = category_repo

    def create_product(self, name: str, price: Decimal, category_id: int ) -> Product:

        category = self.category_repo.get_by_id(category_id=category_id)
        if not category:
            raise ValueError(f"Category with id {category_id} does not exist")

        new_product = Product(id=0, name=name, price=price, category_id=category_id)
        return self.product_repo.create(new_product)
    
    def list_products(self) -> List[Product]:
        return self.product_repo.list_all()
    