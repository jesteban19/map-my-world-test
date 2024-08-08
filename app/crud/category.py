from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.db.models import Category
from app.schemas.category import CategoryCreate


class CRUDCategory(CRUDBase[Category, CategoryCreate]):
    def get_by_name(self, db: Session, *, name: str) -> Category:
        return db.query(Category).filter(Category.name == name).first()


category = CRUDCategory(Category)
