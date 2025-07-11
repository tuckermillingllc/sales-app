from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_dealer_category

router = APIRouter()

@router.get("/dashboard/stats")
def get_dashboard_stats(db: Session = Depends(deps.get_db)):
    return {
        "active_count": crud_dealer_category.count_active_dealers(db),
        "attention_count": crud_dealer_category.count_dealers_needing_attention(db),
        "active_dealers": crud_dealer_category.get_active_dealers(db),
        "attention_dealers": crud_dealer_category.get_attention_dealers(db)
    }
