from app.services.marketplace import MarketplaceService
from app.auth.identity import IdentityContext

marketplace_service = MarketplaceService()

async def search_marketplace_tool(
    identity: IdentityContext,
    query: str
) -> list[dict]:
    """Search Concept Place for automations, scripts, or AI agents."""
    if not identity.has_scope("marketplace:read"):
        raise PermissionError("Insufficient scope: marketplace:read required")

    listings = await marketplace_service.search_marketplace(identity.tenant_id, query)
    return [listing.model_dump() for listing in listings]