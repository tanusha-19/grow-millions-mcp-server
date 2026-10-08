import pytest
from app.auth.identity import IdentityContext
from app.mcp.tools.auto_post import create_post_draft_tool, schedule_post_tool

@pytest.mark.asyncio
async def test_create_post_draft_success():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["social:write"]
    )
    result = await create_post_draft_tool(identity, content_id="cnt_dev_101")
    assert result["tenant_id"] == "tenant_dev_01"
    assert result["post_id"] == "pst_dev_202"
    assert result["status"] == "draft"

@pytest.mark.asyncio
async def test_schedule_post_permission_denied():
    identity = IdentityContext(
        user_id="user_dev_01",
        tenant_id="tenant_dev_01",
        scopes=["social:write"]  # Missing social:publish
    )
    with pytest.raises(PermissionError):
        await schedule_post_tool(identity, post_id="pst_dev_202", scheduled_time="2026-10-10T10:00:00Z")