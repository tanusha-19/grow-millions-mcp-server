import httpx
from typing import Any, Dict, Optional

class BaseHTTPClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def _get_headers(self, tenant_id: str) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "X-Tenant-ID": tenant_id
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    async def get(self, endpoint: str, tenant_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}{endpoint}",
                headers=self._get_headers(tenant_id),
                params=params
            )
            response.raise_for_status()
            return response.json()

    async def post(self, endpoint: str, tenant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}{endpoint}",
                headers=self._get_headers(tenant_id),
                json=payload
            )
            response.raise_for_status()
            return response.json()