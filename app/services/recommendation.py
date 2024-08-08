from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.db.models import LocationCategoryReviewed


def get_recommendations_service(db: Session):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    stale_reviews = db.query(LocationCategoryReviewed) \
        .filter(
        or_(
            LocationCategoryReviewed.last_reviewed_at.is_(None),  # Nunca revisado
            LocationCategoryReviewed.last_reviewed_at < thirty_days_ago  # Revisado hace más de 30 días
        )
    ) \
        .order_by(LocationCategoryReviewed.last_reviewed_at.is_(None).desc(),  # Prioriza los no revisados
                  LocationCategoryReviewed.last_reviewed_at) \
        .limit(10) \
        .all()
    return stale_reviews
