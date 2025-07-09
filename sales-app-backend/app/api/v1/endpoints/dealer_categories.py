from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.dealer_category import DealerCategory, DealerCategoryCreate
from app.crud import crud_dealer_category
from app.api import deps
from typing import List

router = APIRouter()

@router.get("/", response_model=List[DealerCategory])
def read_dealer_categories(db: Session = Depends(deps.get_db)):
    return crud_dealer_category.get_dealer_categories(db)

@router.post("/", response_model=DealerCategory)
def create_dealer_category(category: DealerCategoryCreate, db: Session = Depends(deps.get_db)):
    return crud_dealer_category.create_dealer_category(db, category)
