from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.location import LocationCreate, Location
from app.crud import location as crud_location
from app.crud import location_category_reviewed as lcr
from app.api.dependencies.database import get_db
from app.schemas.location_category_reviewed import LocationCategoryReviewedCreate
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/", response_model=Location)
def create_location(location_in: LocationCreate, db: Session = Depends(get_db)):
    try:
        obj = crud_location.location.create(db=db, obj_in=location_in)
        # create default row in table related for better performance in query
        related_default = LocationCategoryReviewedCreate(location_id=obj.id, category_id=None,
                                                         last_reviewed_at=None)
        lcr.location_category_reviewed.create(db=db, obj_in=related_default)
        return obj
    except Exception as ex:
        raise HTTPException(status_code=400, detail=ex.__str__())


@router.get("/", response_model=List[Location])
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    locations = crud_location.location.get_multi(db, skip=skip, limit=limit)
    return locations
