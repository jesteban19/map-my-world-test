from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.crud import location_category_reviewed as crud_reviewed
from app.schemas.location_category_reviewed import LocationCategoryReviewed
from app.api.dependencies.database import get_db

router = APIRouter()


@router.get("/recommendations/", response_model=List[LocationCategoryReviewed])
def get_recommendations(db: Session = Depends(get_db)):
    recommendations = crud_reviewed.location_category_reviewed.get_reviews(db)
    return recommendations
