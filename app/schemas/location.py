from pydantic import BaseModel, Field


class LocationBase(BaseModel):
    latitude: float = Field(..., description="Latitude of the location in decimal degrees.", example=40.7128)
    longitude: float = Field(..., description="Longitude of the location in decimal degrees.", example=-74.0060)


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int = Field(..., description="Unique identifier for the location.", example=1)

    class Config:
        orm_mode = True
