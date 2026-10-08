from pydantic import BaseModel, Field
from typing import Optional, List

class BusinessProfile(BaseModel):
    tenant_id: str
    business_name: str
    industry: str
    target_audience: str
    brand_voice: Optional[str] = "Professional"

class MarketingStrategy(BaseModel):
    tenant_id: str
    summary: str
    key_objectives: List[str] = Field(default_factory=list)
    channels: List[str] = Field(default_factory=list)