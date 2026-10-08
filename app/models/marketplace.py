from pydantic import BaseModel
from typing import Optional, List

class MarketplaceListing(BaseModel):
    listing_id: str
    title: str
    category: str
    description: str
    price_inr: float
    developer: str
    rating: float = 5.0