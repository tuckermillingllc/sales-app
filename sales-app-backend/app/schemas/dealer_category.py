from pydantic import BaseModel
from typing import Optional

class DealerCategoryBase(BaseModel):
    dealer_id: str
    dealer_name: str
    salesperson: str
    total_bags: int
    bags_ultra_premium: int
    bags_premium: int
    bags_advantage: int
    bags_economy: int
    pct_ultra_premium: float
    pct_premium: float
    pct_advantage: float
    pct_economy: float
    avg_bags_per_order: float
    product_lines: int
    product_engagement: str
    avg_days_between_orders: float
    purchase_frequency: str

    class Config:
        orm_mode = True

class DealerCategoryCreate(DealerCategoryBase):
    pass

class DealerCategory(DealerCategoryBase):
    pass
