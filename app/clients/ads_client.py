from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class AdsClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "META_ADS_BASE_URL", "http://localhost:8005")
        super().__init__(base_url=base_url)

    async def create_campaign_draft(self, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.post("/api/v1/ads/campaigns/draft", tenant_id=tenant_id, payload=payload)

    async def publish_campaign(self, tenant_id: str, campaign_id: str) -> Dict[str, Any]:
        return await self.post(f"/api/v1/ads/campaigns/{campaign_id}/publish", tenant_id=tenant_id, payload={})