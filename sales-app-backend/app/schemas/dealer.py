from pydantic import BaseModel
from typing import Optional

class DealerBase(BaseModel):
    dealer_name: str
    salesperson: Optional[str] = None
    total_bags: Optional[int] = 0
    bags_ultra_premium: Optional[int] = 0
    bags_premium: Optional[int] = 0
    bags_advantage: Optional[int] = 0
    bags_economy: Optional[int] = 0
    pct_ultra_premium: Optional[float] = 0.0
    pct_premium: Optional[float] = 0.0
    pct_advantage: Optional[float] = 0.0
    pct_economy: Optional[float] = 0.0
    avg_bags_per_order: Optional[float] = 0.0
    product_lines: Optional[int] = 0
    product_engagement: Optional[str] = None
    avg_days_between_orders: Optional[float] = None
    purchase_frequency: Optional[str] = None

class DealerCreate(DealerBase):
    dealer_id: int

class DealerUpdate(BaseModel):
    dealer_name: Optional[str] = None
    salesperson: Optional[str] = None
    total_bags: Optional[int] = None
    avg_days_between_orders: Optional[float] = None
    purchase_frequency: Optional[str] = None
    # Add other fields as needed

class Dealer(DealerBase):
    dealer_id: int

    class Config:
        orm_mode = True
