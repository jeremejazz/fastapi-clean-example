from abc import ABC
from typing import List, Optional

from app.domain.models import Product, Category


class ProductRepository(ABC):
    @classmethod
    def create(self, product: Product) -> Product:
        pass
    
    @classmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @classmethod
    def list_all(self) -> List[Product]:
        pass

class CategoryRepository(ABC):
    
    @classmethod
    def create(self, category: Category) -> Category:
        pass

    @classmethod
    def get_by_id(self, category_id: int) -> Optional[Category]:
        pass

