from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class MarketplaceClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "MARKETPLACE_BASE_URL", "http://localhost:8007")
        super().__init__(base_url=base_url)

    async def search_marketplace(self, tenant_id: str, query: str) -> Dict[str, Any]:
        return await self.get("/api/v1/marketplace/search", tenant_id=tenant_id, params={"query": query})