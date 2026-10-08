import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.mark_ai import get_business_profile_tool, get_marketing_strategy_tool

@pytest.mark.asyncio
async def test_get_business_profile_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["business:read"]
    )
    result = await get_business_profile_tool(identity)
    assert result["tenant_id"] == "tenant_dev_01"
    assert "business_name" in result

@pytest.mark.asyncio
async def test_get_business_profile_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=[]  # Missing business:read
    )
    with pytest.raises(PermissionError):
        await get_business_profile_tool(identity)

@pytest.mark.asyncio
async def test_get_marketing_strategy_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["marketing:read"]
    )
    result = await get_marketing_strategy_tool(identity)
    assert result["tenant_id"] == "tenant_dev_01"
    assert "summary" in result