from app.services.mark_ai import MarkAIService
from app.auth.identity import IdentityContext

mark_ai_service = MarkAIService()

async def get_business_profile_tool(identity: IdentityContext) -> dict:
    """Fetch business profile for the authenticated tenant."""
    if not identity.has_scope("business:read"):
        raise PermissionError("Insufficient scope: business:read required")
    profile = await mark_ai_service.get_business_profile(identity.tenant_id)
    return profile.model_dump()

async def get_marketing_strategy_tool(identity: IdentityContext) -> dict:
    """Fetch current marketing strategy for the authenticated tenant."""
    if not identity.has_scope("marketing:read"):
        raise PermissionError("Insufficient scope: marketing:read required")
    strategy = await mark_ai_service.get_marketing_strategy(identity.tenant_id)
    return strategy.model_dump()