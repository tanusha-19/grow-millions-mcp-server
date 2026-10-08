from fastapi import FastAPI, Request
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from app.config.settings import settings
from app.middleware.security import SecurityMiddleware

# Initialize FastMCP Server
mcp = FastMCP(settings.MCP_SERVER_NAME)

@mcp.tool()
async def ping() -> str:
    """Basic ping tool to verify MCP server connectivity."""
    return "pong"

# Initialize FastAPI App
app = FastAPI(
    title="Grow Millions MCP Server",
    version=settings.MCP_SERVER_VERSION,
    description="Standardized integration layer for Single Prompt OS and Grow Millions modules."
)
# Attach Security & Tenant Isolation Middleware
app.add_middleware(SecurityMiddleware)

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring and AWS deployment."""
    return {
        "status": "healthy",
        "server": settings.MCP_SERVER_NAME,
        "version": settings.MCP_SERVER_VERSION
    }

# Set up MCP SSE Server Transport
sse = SseServerTransport("/messages/")

@app.get("/sse")
async def handle_sse(request: Request):
    async with sse.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await mcp._mcp_server.run(
            streams[0],
            streams[1],
            mcp._mcp_server.create_initialization_options(),
        )

@app.post("/messages/")
async def handle_messages(request: Request):
    await sse.handle_post_message(request.scope, request.receive, request._send)