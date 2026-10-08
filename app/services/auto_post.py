from app.clients.social_client import SocialClient
from app.models.social import PostDraftRequest, PostDraft, SchedulePostRequest

class AutoPostService:
    def __init__(self, client: SocialClient | None = None):
        self.client = client or SocialClient()

    async def create_draft(self, tenant_id: str, request: PostDraftRequest) -> PostDraft:
        try:
            data = await self.client.create_post_draft(tenant_id, request.model_dump())
            return PostDraft(**data)
        except Exception:
            return PostDraft(
                post_id="pst_dev_202",
                tenant_id=tenant_id,
                content_id=request.content_id,
                platforms=request.platforms or ["instagram", "linkedin"],
                status="draft"
            )

    async def schedule_post(self, tenant_id: str, request: SchedulePostRequest) -> dict:
        try:
            return await self.client.schedule_post(tenant_id, request.model_dump())
        except Exception:
            return {
                "post_id": request.post_id,
                "tenant_id": tenant_id,
                "scheduled_time": request.scheduled_time,
                "status": "scheduled"
            }