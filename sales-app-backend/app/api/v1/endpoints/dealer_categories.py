# backend/app/api/v1/endpoints/dealer_categories.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import asyncpg
import os

router = APIRouter()

class DealerCategory(BaseModel):
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

@router.post("/dealer-categories/")
async def upload_dealer_categories(data: List[DealerCategory]):
    conn = await asyncpg.connect(dsn=os.getenv("DATABASE_URL"))
    try:
        await conn.execute("TRUNCATE TABLE sales_app.dealer_categories;")
        insert_query = """
            INSERT INTO sales_app.dealer_categories (
                dealer_id, dealer_name, salesperson, total_bags,
                bags_ultra_premium, bags_premium, bags_advantage, bags_economy,
                pct_ultra_premium, pct_premium, pct_advantage, pct_economy,
                avg_bags_per_order, product_lines, product_engagement,
                avg_days_between_orders, purchase_frequency
            ) VALUES (
                $1, $2, $3, $4,
                $5, $6, $7, $8,
                $9, $10, $11, $12,
                $13, $14, $15,
                $16, $17
            )
        """
        for row in data:
            await conn.execute(insert_query, *row.dict().values())
        return {"status": "success", "rows": len(data)}
    finally:
        await conn.close()

@router.get("/dealer-categories/", response_model=List[DealerCategory])
async def get_dealer_categories():
    conn = await asyncpg.connect(dsn=os.getenv("DATABASE_URL"))
    try:
        records = await conn.fetch("SELECT * FROM sales_app.dealer_categories;")
        return [DealerCategory(**dict(row)) for row in records]
    finally:
        await conn.close()
