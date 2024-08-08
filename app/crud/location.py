from app.crud.base import CRUDBase
from app.db.models import Location
from app.schemas.location import LocationCreate


class CRUDLocation(CRUDBase[Location, LocationCreate]):
    pass


location = CRUDLocation(Location)
