import pytest
from app.mcp.server import mcp

@pytest.mark.asyncio
async def test_single_prompt_end_to_end_orchestration():
    identity_data = {
        "tenant_id": "tenant_test_123",
        "user_id": "user_test_456",
        "scopes": [
            "marketing:read",
            "content:write",
            "social:write",
            "social:publish",
            "ads:write",
            "compliance:read",
            "marketplace:read",
        ],
    }

    strategy_result = await mcp.call_tool(
        "get_marketing_strategy",
        arguments={"identity": identity_data}
    )
    assert strategy_result is not None

    content_result = await mcp.call_tool(
        "generate_content",
        arguments={
            "topic": "AI Automation Growth",
            "objective": "Brand Awareness",
            "identity": identity_data
        }
    )
    assert content_result is not None

    draft_result = await mcp.call_tool(
        "create_post_draft",
        arguments={
            "content_id": "content_123",
            "platform": "instagram",
            "caption": "Growth Launch",
            "identity": identity_data
        }
    )
    assert draft_result is not None
    ads_result = await mcp.call_tool(
        "create_campaign_draft",
        arguments={
            "campaign_name": "30-Day Growth Campaign",
            "daily_budget": 500.0,
            "target_audience": "Small Business Owners",
            "content_id": "content_123",
            "identity": identity_data
        }
    )
    assert ads_result is not None