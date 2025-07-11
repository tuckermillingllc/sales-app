from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.schemas.dealer_category import DealerCategory as DealerCategorySchema
from app.schemas.dealer_category import DealerCategoryCreate, DealerCategoryUpdate
from app.crud import crud_dealer_category

router = APIRouter()

@router.get("/", response_model=List[DealerCategorySchema])
def read_dealers(db: Session = Depends(deps.get_db)):
    return crud_dealer_category.get_dealer_categories(db)

@router.get("/{dealer_id}", response_model=DealerCategorySchema)
def read_dealer(dealer_id: int, db: Session = Depends(deps.get_db)):
    dealer = crud_dealer_category.get_dealer_category(db, dealer_id)
    if not dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return dealer

@router.post("/", response_model=DealerCategorySchema)
def create_dealer(dealer: DealerCategoryCreate, db: Session = Depends(deps.get_db)):
    return crud_dealer_category.create_dealer_category(db, dealer)

@router.put("/{dealer_id}", response_model=DealerCategorySchema)
def update_dealer(dealer_id: int, dealer_update: DealerCategoryUpdate, db: Session = Depends(deps.get_db)):
    updated = crud_dealer_category.update_dealer_category(db, dealer_id, dealer_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return updated

@router.delete("/{dealer_id}")
def delete_dealer(dealer_id: int, db: Session = Depends(deps.get_db)):
    deleted = crud_dealer_category.delete_dealer_category(db, dealer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return {"message": "Dealer deleted successfully"}
