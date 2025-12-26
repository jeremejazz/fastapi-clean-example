from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models import Product, Category


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        pass
    
    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass

class CategoryRepository(ABC):
    
    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Category]:
        pass

