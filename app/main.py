from typing import Union

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from app.api.schemas import CategoryCreate, CategoryResponse, ProductCreate, ProductResponse
from app.application.usecases.category_service import CategoryService
from app.application.usecases.product_service import ProductService
from app.domain.interfaces import CategoryRepository
from app.infrastructure.database import Base, Engine, Get_db
from app.infrastructure.repositories import SQLAlchemyCategoryRepository, SqlAlchemyProductRepository

Base.metadata.create_all(bind=Engine)
app = FastAPI()


def get_category_service(db: Session = Depends(Get_db)) -> CategoryService:
    repo = SQLAlchemyCategoryRepository(db)
    return CategoryService(repo)

def get_product_service(db: Session = Depends(Get_db)) -> ProductService:
    category_repo = SQLAlchemyCategoryRepository(db)
    product_repo = SqlAlchemyProductRepository(db)

    return ProductService(product_repo=product_repo, category_repo=category_repo)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/categories", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    service: CategoryService = Depends(get_category_service)
):
    try:
        return service.create_category(category.name)
    except ValueError as v:

        raise HTTPException(status_code=400, detail=f"Invalid name: {v}")

@app.get("/categories")
def get_categories(service: CategoryService = Depends(get_category_service)):

    return service.list_categories()


@app.post("/products", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    try:
        return service.create_product(name=product.name, price=product.price, category_id=product.category_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



 