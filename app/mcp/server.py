from mcp.server.fastmcp import FastMCP
from app.config.settings import settings
from app.mcp.tools.mark_ai import get_business_profile_tool, get_marketing_strategy_tool
from app.mcp.tools.strategist import generate_marketing_strategy_tool
from app.mcp.tools.content import generate_content_tool
from app.mcp.tools.auto_post import create_post_draft_tool, schedule_post_tool
from app.mcp.tools.meta_ads import create_campaign_draft_tool, publish_campaign_tool
from app.mcp.tools.compliance import get_upcoming_compliances_tool
from app.mcp.tools.marketplace import search_marketplace_tool

# Import resources and prompts registers
from app.mcp.resources import register_resources
from app.mcp.prompts import register_prompts

# Initialize FastMCP Server
mcp = FastMCP(settings.MCP_SERVER_NAME)

# Register all 7 Grow Millions tool endpoints
mcp.add_tool(get_business_profile_tool, name="get_business_profile")
mcp.add_tool(get_marketing_strategy_tool, name="get_marketing_strategy")
mcp.add_tool(generate_marketing_strategy_tool, name="generate_marketing_strategy")
mcp.add_tool(generate_content_tool, name="generate_content")
mcp.add_tool(create_post_draft_tool, name="create_post_draft")
mcp.add_tool(schedule_post_tool, name="schedule_post")
mcp.add_tool(create_campaign_draft_tool, name="create_campaign_draft")
mcp.add_tool(publish_campaign_tool, name="publish_campaign")
mcp.add_tool(get_upcoming_compliances_tool, name="get_upcoming_compliances")
mcp.add_tool(search_marketplace_tool, name="search_marketplace")

# Register Resources and Prompts
register_resources(mcp)
register_prompts(mcp)

if __name__ == "__main__":
    mcp.run()