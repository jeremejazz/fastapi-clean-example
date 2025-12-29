import pytest

from decimal import Decimal
from typing import List, Optional

from app.application.usecases.product_service import ProductService
from app.domain.interfaces import CategoryRepository, ProductRepository
from app.domain.models import Category, Product

class FakeCategoryRepository(CategoryRepository):
    def __init__(self):
        self.categories = []

    def create(self, category: Category) -> Category:
        category.id = len(self.categories) + 1
        self.categories.append(category)
        return category
    
    def get_by_id(self, category_id: int) -> Optional[Category]:
        for cat in self.categories:
            if cat.id == category_id:
                return cat
            else:
                return None
            
    def get_by_name(self, name):
        return super().get_by_name(name)
    
    def list_all(self):
        return super().list_all()
            
class FakeProductRepository(ProductRepository):
    def __init__(self):
        self.products = []

    def create(self, product: Product) -> Product:
        product.id = len(self.products) + 1
        self.products.append(product)
        return product
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
            else:
                return None

    def list_all(self) -> List[Product]:
        return self.products
 
    
    


def test_create_product_success():

    category_repo = FakeCategoryRepository()
    product_repo = FakeProductRepository()

    service = ProductService(product_repo, category_repo)

    category_repo.create(Category(id=0, name="Electronics"))

    new_product = service.create_product(
        name="Laptop",
        price=Decimal(99.99),
        category_id=1
    )

    assert new_product.id == 1
    assert new_product.name == "Laptop"
    assert new_product.price == Decimal(99.99)
    assert len(product_repo.products) == 1


            

    