from app.services.meta_ads import MetaAdsService
from app.auth.identity import IdentityContext
from app.models.ads import CampaignDraftRequest

meta_ads_service = MetaAdsService()

async def create_campaign_draft_tool(
    identity: IdentityContext,
    campaign_name: str,
    daily_budget: float,
    target_audience: str,
    content_id: str
) -> dict:
    """Create a Meta Ads campaign draft (Safe write action)."""
    if not identity.has_scope("ads:write"):
        raise PermissionError("Insufficient scope: ads:write required")

    request = CampaignDraftRequest(
        campaign_name=campaign_name,
        daily_budget=daily_budget,
        target_audience=target_audience,
        content_id=content_id
    )
    campaign = await meta_ads_service.create_campaign_draft(identity.tenant_id, request)
    return campaign.model_dump()

async def publish_campaign_tool(
    identity: IdentityContext,
    campaign_id: str
) -> dict:
    """Publish a Meta Ads campaign to spend budget (High-risk action requiring ads:publish permission)."""
    if not identity.has_scope("ads:publish"):
        raise PermissionError("Insufficient scope: ads:publish required")

    return await meta_ads_service.publish_campaign(identity.tenant_id, campaign_id)