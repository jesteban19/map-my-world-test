from fastapi import FastAPI
from app.api.v1.endpoints import categories, locations, recommendations

app = FastAPI()

app.include_router(categories.router, prefix="/v1/categories", tags=["categories"])
app.include_router(locations.router, prefix="/v1/locations", tags=["locations"])
app.include_router(recommendations.router, prefix="/v1", tags=["recommendations"])
