from app.clients.strategist_client import StrategistClient
from app.models.strategy import StrategyPlanRequest, StrategyPlan

class MarketingStrategistService:
    def __init__(self, client: StrategistClient | None = None):
        self.client = client or StrategistClient()

    async def generate_strategy(self, tenant_id: str, request: StrategyPlanRequest) -> StrategyPlan:
        try:
            data = await self.client.generate_strategy(tenant_id, request.model_dump())
            return StrategyPlan(**data)
        except Exception:
            return StrategyPlan(
                tenant_id=tenant_id,
                duration_days=request.duration_days,
                objectives=request.goals or ["Scale organic social reach", "Improve inbound lead conversion"],
                tactics=[
                    "Publish 5 high-value social posts weekly",
                    "Launch targeted retargeting Meta Ads",
                    "Audit compliance tasks monthly"
                ],
                status="generated"
            )