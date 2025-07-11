from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.feed_product_mapping import FeedProductMapping, FeedProductMappingCreate, FeedProductMappingUpdate
from app.crud import crud_feed_product_mapping
from app.api import deps
from typing import List

router = APIRouter()

@router.get("/", response_model=List[FeedProductMapping])
def read_feed_product_mappings(db: Session = Depends(deps.get_db)):
    return crud_feed_product_mapping.get_feed_product_mappings(db)

@router.post("/", response_model=FeedProductMapping)
def create_feed_product_mapping(mapping: FeedProductMappingCreate, db: Session = Depends(deps.get_db)):
    return crud_feed_product_mapping.create_feed_product_mapping(db, mapping)

@router.get("/{mapping_id}", response_model=FeedProductMapping)
def read_feed_product_mapping(mapping_id: int, db: Session = Depends(deps.get_db)):
    mapping = crud_feed_product_mapping.get_feed_product_mapping(db, mapping_id)
    if not mapping:
        raise HTTPException(status_code=404, detail="Feed product mapping not found")
    return mapping

@router.put("/{mapping_id}", response_model=FeedProductMapping)
def update_feed_product_mapping(mapping_id: int, mapping: FeedProductMappingUpdate, db: Session = Depends(deps.get_db)):
    updated_mapping = crud_feed_product_mapping.update_feed_product_mapping(db, mapping_id, mapping)
    if not updated_mapping:
        raise HTTPException(status_code=404, detail="Feed product mapping not found")
    return updated_mapping

@router.delete("/{mapping_id}")
def delete_feed_product_mapping(mapping_id: int, db: Session = Depends(deps.get_db)):
    mapping = crud_feed_product_mapping.delete_feed_product_mapping(db, mapping_id)
    if not mapping:
        raise HTTPException(status_code=404, detail="Feed product mapping not found")
    return {"message": "Feed product mapping deleted successfully"}