from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import deps
from app.schemas import DealerCategory, DealerCategoryCreate, DealerCategoryUpdate
from app.crud import crud_dealer_category

router = APIRouter()

@router.get("/", response_model=List[DealerCategory])
def read_dealer_categories(db: Session = Depends(deps.get_db)):
    return crud_dealer_category.get_dealer_categories(db)

@router.post("/", response_model=DealerCategory)
def create_dealer_category(category: DealerCategoryCreate, db: Session = Depends(deps.get_db)):
    return crud_dealer_category.create_dealer_category(db, category)

@router.get("/{category_id}", response_model=DealerCategory)
def read_dealer_category(category_id: int, db: Session = Depends(deps.get_db)):
    category = crud_dealer_category.get_dealer_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Dealer category not found")
    return category

@router.put("/{category_id}", response_model=DealerCategory)
def update_dealer_category(category_id: int, category: DealerCategoryUpdate, db: Session = Depends(deps.get_db)):
    updated_category = crud_dealer_category.update_dealer_category(db, category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Dealer category not found")
    return updated_category

@router.delete("/{category_id}")
def delete_dealer_category(category_id: int, db: Session = Depends(deps.get_db)):
    deleted_category = crud_dealer_category.delete_dealer_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Dealer category not found")
    return {"message": "Dealer category deleted successfully"}
