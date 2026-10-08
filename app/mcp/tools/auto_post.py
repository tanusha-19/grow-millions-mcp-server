from app.services.auto_post import AutoPostService
from app.auth.identity import IdentityContext
from app.models.social import PostDraftRequest, SchedulePostRequest

auto_post_service = AutoPostService()

async def create_post_draft_tool(
    identity: IdentityContext,
    content_id: str,
    platforms: list[str] | None = None
) -> dict:
    """Create a social media post draft."""
    if not identity.has_scope("social:write"):
        raise PermissionError("Insufficient scope: social:write required")

    request = PostDraftRequest(
        content_id=content_id,
        platforms=platforms or ["instagram"]
    )
    draft = await auto_post_service.create_draft(identity.tenant_id, request)
    return draft.model_dump()

async def schedule_post_tool(
    identity: IdentityContext,
    post_id: str,
    scheduled_time: str
) -> dict:
    """Schedule a post for publishing (High-risk action)."""
    if not identity.has_scope("social:publish"):
        raise PermissionError("Insufficient scope: social:publish required")

    request = SchedulePostRequest(
        post_id=post_id,
        scheduled_time=scheduled_time
    )
    return await auto_post_service.schedule_post(identity.tenant_id, request)