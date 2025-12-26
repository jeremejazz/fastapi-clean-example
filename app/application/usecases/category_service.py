
from app.domain.interfaces import CategoryRepository
from app.domain.models import Category


class CategoryService:
    def __init__(self, repostitory: CategoryRepository):
        self.repository = repostitory

    def create_category(self, name: str) -> Category:
        new_category = Category(id=0, name=name)
        return self.repository.create(new_category)
    
    def get_category(self, category_id:int) -> Category:
        return self.repository.get_by_id(category_id)