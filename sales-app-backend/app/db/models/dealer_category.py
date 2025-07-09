from sqlalchemy import Column, Integer, String, Numeric
from app.db.base_class import Base

class DealerCategory(Base):
    __tablename__ = "dealer_categories"
    __table_args__ = {"schema": "sales_app"}

    dealer_id = Column(String, primary_key=True)
    dealer_name = Column(String)
    salesperson = Column(String)
    total_bags = Column(Integer)
    bags_ultra_premium = Column(Integer)
    bags_premium = Column(Integer)
    bags_advantage = Column(Integer)
    bags_economy = Column(Integer)
    pct_ultra_premium = Column(Numeric(7,3))
    pct_premium = Column(Numeric(7,3))
    pct_advantage = Column(Numeric(7,3))
    pct_economy = Column(Numeric(7,3))
    avg_bags_per_order = Column(Numeric(7,3))
    product_lines = Column(Integer)
    product_engagement = Column(String)
    avg_days_between_orders = Column(Numeric(7,3))
    purchase_frequency = Column(String)
