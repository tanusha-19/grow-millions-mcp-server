import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.meta_ads import create_campaign_draft_tool, publish_campaign_tool

@pytest.mark.asyncio
async def test_create_campaign_draft_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["ads:write"]
    )
    result = await create_campaign_draft_tool(
        identity,
        campaign_name="Q4 Growth Campaign",
        daily_budget=500.0,
        target_audience="Small Business Owners",
        content_id="cnt_dev_101"
    )
    assert result["tenant_id"] == "tenant_dev_01"
    assert result["campaign_id"] == "cmp_dev_303"
    assert result["status"] == "draft"

@pytest.mark.asyncio
async def test_publish_campaign_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["ads:write"]  # Lacks ads:publish permission
    )
    with pytest.raises(PermissionError):
        await publish_campaign_tool(identity, campaign_id="cmp_dev_303")