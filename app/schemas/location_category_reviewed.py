from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: Optional[int]
    last_reviewed_at: Optional[datetime]


class LocationCategoryReviewed(LocationCategoryReviewedBase):
    class Config:
        orm_mode = True


class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass
