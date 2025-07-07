# backend/app/api/v1/endpoints/customers.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.customer import Customer, CustomerCreate
from app.crud.crud_customer import get_customers, create_customer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Customer])
def read_customers(db: Session = Depends(get_db)):
    return get_customers(db)

@router.post("/", response_model=Customer)
def add_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)