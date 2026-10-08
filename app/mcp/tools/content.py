from app.services.content_generator import ContentGeneratorService
from app.auth.identity import IdentityContext
from app.models.content import ContentRequest

content_service = ContentGeneratorService()

async def generate_content_tool(
    identity: IdentityContext,
    topic: str,
    platform: str = "instagram",
    format: str = "post",
    tone: str = "engaging"
) -> dict:
    """Generate social content draft for the authenticated tenant."""
    if not identity.has_scope("content:write"):
        raise PermissionError("Insufficient scope: content:write required")

    request = ContentRequest(
        topic=topic,
        platform=platform,
        format=format,
        tone=tone
    )
    asset = await content_service.generate_content(identity.tenant_id, request)
    return asset.model_dump()