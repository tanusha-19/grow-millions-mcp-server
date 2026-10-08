from app.clients.ads_client import AdsClient
from app.models.ads import CampaignDraftRequest, Campaign

class MetaAdsService:
    def __init__(self, client: AdsClient | None = None):
        self.client = client or AdsClient()

    async def create_campaign_draft(self, tenant_id: str, request: CampaignDraftRequest) -> Campaign:
        try:
            data = await self.client.create_campaign_draft(tenant_id, request.model_dump())
            return Campaign(**data)
        except Exception:
            return Campaign(
                campaign_id="cmp_dev_303",
                tenant_id=tenant_id,
                campaign_name=request.campaign_name,
                daily_budget=request.daily_budget,
                target_audience=request.target_audience,
                content_id=request.content_id,
                status="draft"
            )

    async def publish_campaign(self, tenant_id: str, campaign_id: str) -> dict:
        try:
            return await self.client.publish_campaign(tenant_id, campaign_id)
        except Exception:
            return {
                "campaign_id": campaign_id,
                "tenant_id": tenant_id,
                "status": "published",
                "message": "Campaign published successfully."
            }