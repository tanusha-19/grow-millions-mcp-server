from typing import Dict, Any
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class StrategistClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "STRATEGIST_BASE_URL", "http://localhost:8002")
        super().__init__(base_url=base_url)

    async def generate_strategy(self, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self.post("/api/v1/strategy/generate", tenant_id=tenant_id, payload=payload)