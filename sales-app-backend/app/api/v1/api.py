from fastapi import APIRouter
from .endpoints import customers, dealer_categories, feed_product_mapping, dashboard

api_router = APIRouter()
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(dealer_categories.router, prefix="/dealer-categories", tags=["dealer-categories"])
api_router.include_router(feed_product_mapping.router, prefix="/feed-product-mapping", tags=["feed-product-mapping"])
api_router.include_router(dashboard.router, prefix="/api/v1", tags=["dashboard"])