from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("LocationCategoryReviewed", back_populates="location")


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    reviews = relationship("LocationCategoryReviewed", back_populates="category")


class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    last_reviewed_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)

    location = relationship("Location", back_populates="reviews")
    category = relationship("Category", back_populates="reviews")
