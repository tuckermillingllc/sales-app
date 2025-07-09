from fastapi import APIRouter
from .endpoints import customers, dealer_categories

api_router = APIRouter()
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(dealer_categories.router, prefix="/dealer-categories", tags=["dealer-categories"])