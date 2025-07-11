from sqlalchemy.orm import Session
from app.schemas.feed_product_mapping import FeedProductMappingCreate, FeedProductMappingUpdate
# You'll need to import your FeedProductMapping model from wherever it's located

def get_feed_product_mappings(db: Session):
    return db.query(FeedProductMapping).all()

def get_feed_product_mapping(db: Session, mapping_id: int):
    return db.query(FeedProductMapping).filter(FeedProductMapping.id == mapping_id).first()

def create_feed_product_mapping(db: Session, mapping: FeedProductMappingCreate):
    db_mapping = FeedProductMapping(**mapping.dict())
    db.add(db_mapping)
    db.commit()
    db.refresh(db_mapping)
    return db_mapping

def update_feed_product_mapping(db: Session, mapping_id: int, mapping: FeedProductMappingUpdate):
    db_mapping = db.query(FeedProductMapping).filter(FeedProductMapping.id == mapping_id).first()
    if db_mapping:
        for key, value in mapping.dict(exclude_unset=True).items():
            setattr(db_mapping, key, value)
        db.commit()
        db.refresh(db_mapping)
    return db_mapping

def delete_feed_product_mapping(db: Session, mapping_id: int):
    db_mapping = db.query(FeedProductMapping).filter(FeedProductMapping.id == mapping_id).first()
    if db_mapping:
        db.delete(db_mapping)
        db.commit()
    return db_mapping