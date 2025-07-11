from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from app.db.models.dealer_category import DealerCategory
from app.schemas.dealer_category import DealerCategoryCreate, DealerCategoryBase


def get_dealer_categories(db: Session):
    """Return all dealer categories."""
    return db.query(DealerCategory).all()


def get_dealer_category(db: Session, category_id: int):
    """Return a single dealer category by ID."""
    return db.query(DealerCategory).filter(DealerCategory.id == category_id).first()


def create_dealer_category(db: Session, category: DealerCategoryCreate):
    """Create a new dealer category."""
    db_category = DealerCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_dealer_category(db: Session, category_id: int, category_update: DealerCategoryBase):
    """Update an existing dealer category by ID."""
    db_category = db.query(DealerCategory).filter(DealerCategory.id == category_id).first()
    if not db_category:
        return None
    for field, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, field, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_dealer_category(db: Session, category_id: int):
    """Delete a dealer category by ID."""
    db_category = db.query(DealerCategory).filter(DealerCategory.id == category_id).first()
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category

def count_active_dealers(db: Session) -> int:
    """Dealers with avg_days_between_orders <= 45"""
    return db.query(DealerCategory).filter(DealerCategory.avg_days_between_orders <= 45).count()

from sqlalchemy import func

def count_dealers_needing_attention(db: Session) -> int:
    """Dealers with avg_days_between_orders > 45 or 'sporadic'/null frequency (case-insensitive)"""
    return db.query(func.count(DealerCategory.dealer_id)).filter(
        or_(
            DealerCategory.avg_days_between_orders > 45,
            DealerCategory.purchase_frequency == None,
            func.lower(DealerCategory.purchase_frequency) == "sporadic"
        )
    ).scalar()


def get_active_dealers(db: Session) -> list[dict]:
    """Top active dealers with placeholder growth metrics"""
    rows = db.query(DealerCategory).filter(DealerCategory.avg_days_between_orders <= 45).limit(10).all()
    return [
        {
            "id": row.dealer_id,
            "name": row.dealer_name,
            "status": "active",
            "metric": "+12%",  # Placeholder — update with real calculation if available
            "metricType": "positive"
        }
        for row in rows
    ]

def get_attention_dealers(db: Session) -> list[dict]:
    """Dealers who need attention due to inactivity or low frequency"""
    rows = db.query(DealerCategory).filter(
        or_(
            DealerCategory.avg_days_between_orders > 45,
            DealerCategory.purchase_frequency == None,
            DealerCategory.purchase_frequency.ilike("sporadic")
        )
    ).limit(10).all()
    return [
        {
            "id": row.dealer_id,
            "name": row.dealer_name,
            "status": "declining",  # You could customize based on how "stopped" is defined
            "metric": "-25%",  # Placeholder
            "metricType": "negative"
        }
        for row in rows
    ]