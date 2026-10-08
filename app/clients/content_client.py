from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class ContentClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "CONTENT_BASE_URL", "http://localhost:8003")
        super().__init__(base_url=base_url)

    async def generate_content(self, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.post("/api/v1/content/generate", tenant_id=tenant_id, payload=payload)