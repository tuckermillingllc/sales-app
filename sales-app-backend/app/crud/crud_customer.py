# backend/app/crud/crud_customer.py
from sqlalchemy.orm import Session
from app.db.models.customer import Customer
from app.schemas.customer import CustomerCreate

def get_customers(db: Session):
    return db.query(Customer).all()

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer
