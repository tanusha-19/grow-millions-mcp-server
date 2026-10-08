"""MCP Resources registration for GrowMillions MCP server."""

from mcp.server.fastmcp import FastMCP
from app.services.mark_ai import MarkAIService
from app.services.compliance import ComplianceService


def register_resources(mcp: FastMCP) -> None:
    """Register all URI-based MCP read-only resources."""

    @mcp.resource("growmillions://business/profile")
    async def get_business_profile_resource() -> str:
        """Returns active business profile and brand voice context."""
        service = MarkAIService()
        profile_data = await service.get_business_profile()
        return f"Business Profile Context:\n{profile_data}"

    @mcp.resource("growmillions://compliance/calendar")
    async def get_compliance_calendar_resource() -> str:
        """Returns upcoming GST and compliance deadlines."""
        service = ComplianceService()
        calendar_data = await service.get_upcoming_compliances()
        return f"Compliance Calendar Context:\n{calendar_data}"