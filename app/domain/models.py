from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    category_id: int
    category: Optional[Category] = None