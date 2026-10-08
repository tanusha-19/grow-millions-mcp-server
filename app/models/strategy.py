from pydantic import BaseModel, Field
from typing import List, Optional

class StrategyPlanRequest(BaseModel):
    duration_days: int = 30
    goals: List[str] = Field(default_factory=list)

class StrategyPlan(BaseModel):
    tenant_id: str
    duration_days: int
    objectives: List[str]
    tactics: List[str]
    status: str = "active"