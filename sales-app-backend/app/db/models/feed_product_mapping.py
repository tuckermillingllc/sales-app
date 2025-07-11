from pydantic import BaseModel
from typing import Optional

class FeedProductMappingBase(BaseModel):
    species: Optional[str] = None
    competitor: Optional[str] = None
    competitor_product: Optional[str] = None
    competitor_feed_form: Optional[str] = None
    competitor_density: Optional[float] = None
    competitor_retail_price: Optional[float] = None
    tucker_product: Optional[str] = None
    tucker_feed_form: Optional[str] = None
    tucker_dealer_price: Optional[float] = None

class FeedProductMappingCreate(FeedProductMappingBase):
    pass

class FeedProductMappingUpdate(FeedProductMappingBase):
    pass

class FeedProductMapping(FeedProductMappingBase):
    id: int
    
    class Config:
        from_attributes = True