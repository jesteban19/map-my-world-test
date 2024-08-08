from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., description="The name of the category.", example="Restaurant")


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int = Field(..., description="Unique identifier for the category.", example=1)

    class Config:
        orm_mode = True
