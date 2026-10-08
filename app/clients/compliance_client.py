from typing import Dict, Any, List
from app.clients.http import BaseHTTPClient
from app.config.settings import settings

class ComplianceClient(BaseHTTPClient):
    def __init__(self):
        base_url = getattr(settings, "COMPLIANCE_BASE_URL", "http://localhost:8006")
        super().__init__(base_url=base_url)

    async def get_upcoming_compliances(self, tenant_id: str) -> Any:
        return await self.get("/api/v1/compliance/upcoming", tenant_id=tenant_id)