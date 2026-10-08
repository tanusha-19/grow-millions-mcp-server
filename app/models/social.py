from pydantic import BaseModel, Field
from typing import Optional, List

class PostDraftRequest(BaseModel):
    content_id: str
    platforms: List[str] = Field(default_factory=list)

class PostDraft(BaseModel):
    post_id: str
    tenant_id: str
    content_id: str
    platforms: List[str]
    status: str = "draft"

class SchedulePostRequest(BaseModel):
    post_id: str
    scheduled_time: str