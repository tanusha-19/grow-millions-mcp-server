from app.clients.mark_ai_client import MarkAIClient
from app.models.business import BusinessProfile, MarketingStrategy

class MarkAIService:
    def __init__(self, client: MarkAIClient | None = None):
        self.client = client or MarkAIClient()

    async def get_business_profile(self, tenant_id: str) -> BusinessProfile:
        try:
            data = await self.client.get_business_profile(tenant_id)
            return BusinessProfile(**data)
        except Exception:
            # Fallback mock profile for local development
            return BusinessProfile(
                tenant_id=tenant_id,
                business_name="Grow Millions Demo",
                industry="AI & Business Automation",
                target_audience="Founders & Small Businesses",
                brand_voice="Professional & Direct"
            )

    async def get_marketing_strategy(self, tenant_id: str) -> MarketingStrategy:
        try:
            data = await self.client.get_marketing_strategy(tenant_id)
            return MarketingStrategy(**data)
        except Exception:
            # Fallback mock strategy for local development
            return MarketingStrategy(
                tenant_id=tenant_id,
                summary="30-day growth plan focusing on automated content and ad campaigns.",
                key_objectives=["Increase inbound leads by 25%", "Automate daily publishing"],
                channels=["LinkedIn", "Instagram", "Meta Ads"]
            )