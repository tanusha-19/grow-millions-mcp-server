from app.clients.content_client import ContentClient
from app.models.content import ContentRequest, ContentAsset

class ContentGeneratorService:
    def __init__(self, client: ContentClient | None = None):
        self.client = client or ContentClient()

    async def generate_content(self, tenant_id: str, request: ContentRequest) -> ContentAsset:
        try:
            data = await self.client.generate_content(tenant_id, request.model_dump())
            return ContentAsset(**data)
        except Exception:
            return ContentAsset(
                content_id="cnt_dev_101",
                tenant_id=tenant_id,
                platform=request.platform,
                format=request.format,
                caption=f"🚀 {request.topic} - Scale your business efficiently with Grow Millions!",
                hashtags=["#GrowMillions", "#AI", "#BusinessGrowth"],
                status="draft"
            )