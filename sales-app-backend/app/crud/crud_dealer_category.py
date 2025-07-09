from sqlalchemy.orm import Session
from app.db.models.dealer_category import DealerCategory
from app.schemas.dealer_category import DealerCategoryCreate

def get_dealer_categories(db: Session):
    return db.query(DealerCategory).all()

def create_dealer_category(db: Session, category: DealerCategoryCreate):
    db_category = DealerCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
