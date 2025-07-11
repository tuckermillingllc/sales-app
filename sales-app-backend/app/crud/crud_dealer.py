from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.db.models.dealer_category import DealerCategory  # your existing model
from typing import List, Dict

def count_active_dealers(db: Session) -> int:
    return db.query(DealerCategory).filter(DealerCategory.avg_days_between_orders <= 45).count()

def count_dealers_needing_attention(db: Session) -> int:
    return db.query(DealerCategory).filter(
        or_(
            DealerCategory.avg_days_between_orders > 45,
            DealerCategory.purchase_frequency == None,
            DealerCategory.purchase_frequency.ilike("sporadic")
        )
    ).count()

def get_active_dealers(db: Session) -> List[Dict]:
    rows = db.query(DealerCategory).filter(DealerCategory.avg_days_between_orders <= 45).limit(10).all()
    return [
        {
            "id": row.dealer_id,
            "name": row.dealer_name,
            "status": "active",
            "metric": "+12%",  # Replace with real growth if available
            "metricType": "positive"
        }
        for row in rows
    ]

def get_attention_dealers(db: Session) -> List[Dict]:
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
            "status": "declining",
            "metric": "-25%",  # Replace with real metric if available
            "metricType": "negative"
        }
        for row in rows
    ]
