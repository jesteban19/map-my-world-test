from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.crud.base import CRUDBase
from app.db.models import LocationCategoryReviewed
from app.schemas.location_category_reviewed import LocationCategoryReviewedCreate
from app.services.recommendation import get_recommendations_service


class CRUDLocationCategoryReviewed(CRUDBase[LocationCategoryReviewed, LocationCategoryReviewedCreate]):
    def get_reviews(self, db: Session):
        return get_recommendations_service(db=db)


location_category_reviewed = CRUDLocationCategoryReviewed(LocationCategoryReviewed)
