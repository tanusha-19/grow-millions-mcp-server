from pydantic import BaseModel, Field
from typing import List, Optional

class ContentRequest(BaseModel):
    topic: str
    platform: str = "instagram"
    format: str = "post"
    tone: Optional[str] = "engaging"

class ContentAsset(BaseModel):
    content_id: str
    tenant_id: str
    platform: str
    format: str
    caption: str
    hashtags: List[str] = Field(default_factory=list)
    status: str = "draft"