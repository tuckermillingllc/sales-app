from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Customer(Base):
    __tablename__ = "customers"
    __table_args__ = {"schema": "sales_app"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
