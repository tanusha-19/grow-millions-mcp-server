import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.marketplace import search_marketplace_tool

@pytest.mark.asyncio
async def test_search_marketplace_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["marketplace:read"]
    )
    result = await search_marketplace_tool(identity, query="WhatsApp")
    assert isinstance(result, list)
    assert len(result) > 0
    assert "title" in result[0]
    assert result[0]["price_inr"] > 0

@pytest.mark.asyncio
async def test_search_marketplace_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["content:read"]  # Lacks marketplace:read
    )
    with pytest.raises(PermissionError):
        await search_marketplace_tool(identity, query="WhatsApp")