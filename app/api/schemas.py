# app/api/schemas.py
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        form_attributes = True


class ProductCreate(BaseModel):
    name: str
    price: float
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category_id: int