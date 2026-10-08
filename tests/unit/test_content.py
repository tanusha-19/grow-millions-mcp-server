import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.content import generate_content_tool

@pytest.mark.asyncio
async def test_generate_content_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["content:write"]
    )
    result = await generate_content_tool(identity, topic="AI Workflows")
    assert result["tenant_id"] == "tenant_dev_01"
    assert result["content_id"] == "cnt_dev_101"
    assert result["status"] == "draft"

@pytest.mark.asyncio
async def test_generate_content_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["content:read"]  # Lacks content:write
    )
    with pytest.raises(PermissionError):
        await generate_content_tool(identity, topic="AI Workflows")