from pydantic import BaseModel, Field
from typing import Optional

class CampaignDraftRequest(BaseModel):
    campaign_name: str
    daily_budget: float
    target_audience: str
    content_id: str

class Campaign(BaseModel):
    campaign_id: str
    tenant_id: str
    campaign_name: str
    daily_budget: float
    target_audience: str
    content_id: str
    status: str = "draft"  # Lifecycle: draft -> pending_approval -> published