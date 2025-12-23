from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Product:
    id: int
    name: str
    price: float
    category_id: int
    category: Optional[Category] = None