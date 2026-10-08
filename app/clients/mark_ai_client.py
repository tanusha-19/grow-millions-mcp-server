from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class MarkAIClient(BaseHTTPClient):
    def __init__(self):
        # Fallback default URL for local dev
        base_url = getattr(settings, "MARK_AI_BASE_URL", "http://localhost:8001")
        super().__init__(base_url=base_url)

    async def get_business_profile(self, tenant_id: str) -> Dict[str, Any]:
        return await self.get("/api/v1/business/profile", tenant_id=tenant_id)

    async def get_marketing_strategy(self, tenant_id: str) -> Dict[str, Any]:
        return await self.get("/api/v1/strategy", tenant_id=tenant_id)