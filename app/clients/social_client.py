from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class SocialClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "AUTO_POST_BASE_URL", "http://localhost:8004")
        super().__init__(base_url=base_url)

    async def create_post_draft(self, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.post("/api/v1/posts/draft", tenant_id=tenant_id, payload=payload)

    async def schedule_post(self, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.post("/api/v1/posts/schedule", tenant_id=tenant_id, payload=payload)