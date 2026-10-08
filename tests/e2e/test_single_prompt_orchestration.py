import pytest
from app.mcp.server import mcp

@pytest.mark.asyncio
async def test_single_prompt_end_to_end_orchestration():
    """
    Simulates the orchestrator calling tools across multiple modules for a full growth prompt workflow.
    """
    identity_data = {
        "tenant_id": "tenant_test_123",
        "user_id": "user_test_456",
        "scopes": [
            "marketing:read",
            "content:write",
            "social:publish",
            "ads:write",
            "compliance:read",
            "marketplace:read",
        ],
    }

    # 1. Fetch Strategy / Profile
    strategy_result = await mcp.call_tool(
        "get_marketing_strategy", 
        arguments={"identity": identity_data}
    )
    assert strategy_result is not None

    # 2. Generate Content Draft
    content_result = await mcp.call_tool(
        "generate_content", 
        arguments={
            "topic": "AI Automation Growth", 
            "objective": "Brand Awareness", 
            "identity": identity_data
        }
    )
    assert content_result is not None

    # 3. Create Social Post Draft (requires 'content_id', 'platform', 'caption')
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

    # 4. Create Meta Ads Campaign Draft
    ads_result = await mcp.call_tool(
        "create_campaign_draft", 
        arguments={
            "name": "30-Day Growth Campaign", 
            "identity": identity_data
        }
    )
    assert ads_result is not None

    # 5. Check Compliance Calendar
    compliance_result = await mcp.call_tool(
        "get_compliance_calendar", 
        arguments={"identity": identity_data}
    )
    assert compliance_result is not None

    # 6. Search Marketplace
    mkt_result = await mcp.call_tool(
        "search_marketplace", 
        arguments={
            "query": "email automation", 
            "identity": identity_data
        }
    )
    assert mkt_result is not None