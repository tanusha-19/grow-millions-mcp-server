import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.strategist import generate_marketing_strategy_tool

@pytest.mark.asyncio
async def test_generate_strategy_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["marketing:write"]
    )
    result = await generate_marketing_strategy_tool(identity, duration_days=60, goals=["Boost Brand Awareness"])
    assert result["tenant_id"] == "tenant_dev_01"
    assert result["duration_days"] == 60
    assert len(result["tactics"]) > 0

@pytest.mark.asyncio
async def test_generate_strategy_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["marketing:read"]  # Lacks marketing:write
    )
    with pytest.raises(PermissionError):
        await generate_marketing_strategy_tool(identity)