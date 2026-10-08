from pydantic import BaseModel
from typing import Optional

class ComplianceItem(BaseModel):
    item_id: str
    tenant_id: str
    title: str
    due_date: str
    status: str = "pending"
    description: Optional[str] = None