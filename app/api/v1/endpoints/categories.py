from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, Category
from app.crud import category as crud_category
from app.api.dependencies.database import get_db

router = APIRouter()


@router.post("/", response_model=Category)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    category = crud_category.category.get_by_name(db, name=category_in.name)
    if category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud_category.category.create(db=db, obj_in=category_in)


@router.get("/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = crud_category.category.get_multi(db, skip=skip, limit=limit)
    return categories
