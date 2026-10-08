import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.compliance import get_upcoming_compliances_tool

@pytest.mark.asyncio
async def test_get_upcoming_compliances_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["compliance:read"]
    )
    result = await get_upcoming_compliances_tool(identity)
    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0]["tenant_id"] == "tenant_dev_01"
    assert "due_date" in result[0]

@pytest.mark.asyncio
async def test_get_upcoming_compliances_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["marketing:read"]  # Lacks compliance:read
    )
    with pytest.raises(PermissionError):
        await get_upcoming_compliances_tool(identity)