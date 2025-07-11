from sqlalchemy.orm import Session
from app.db.models.dealer_category import DealerCategory
from app.schemas.dealer_category import DealerCategoryCreate, DealerCategoryUpdate


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


def update_dealer_category(db: Session, category_id: int, category_update: DealerCategoryUpdate):
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
