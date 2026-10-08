"""MCP Workflow Prompts for GrowMillions MCP server."""

from mcp.server.fastmcp import FastMCP


def register_prompts(mcp: FastMCP) -> None:
    """Register standardized operational workflow prompts."""

    @mcp.prompt("marketing_campaign_review")
    def marketing_campaign_review_prompt(product_name: str, target_audience: str) -> str:
        """Generates a structured workflow prompt to review and draft a Meta ad campaign."""
        return (
            f"You are the Lead Marketing Strategist for GrowMillions.\n"
            f"Task: Review and prepare a complete ad campaign for '{product_name}' targeted at '{target_audience}'.\n\n"
            f"Steps to execute:\n"
            f"1. Fetch business profile context from 'growmillions://business/profile'.\n"
            f"2. Call `generate_marketing_strategy` for '{product_name}'.\n"
            f"3. Draft copy using `generate_content`.\n"
            f"4. Create campaign draft via `create_campaign_draft` (Do NOT publish without explicit confirmation)."
        )

    @mcp.prompt("weekly_content_planning")
    def weekly_content_planning_prompt(platform: str = "Instagram") -> str:
        """Generates a workflow prompt for scheduling social media content."""
        return (
            f"You are the Content Operations Assistant.\n"
            f"Task: Build a content schedule for platform: '{platform}'.\n\n"
            f"Workflow:\n"
            f"1. Check upcoming events in 'growmillions://compliance/calendar'.\n"
            f"2. Generate 3 post ideas aligned with active deadlines/promotions.\n"
            f"3. Create draft posts using `create_post_draft`.\n"
            f"4. Propose optimal schedule timings using `schedule_post`."
        )