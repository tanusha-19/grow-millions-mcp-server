# GrowMillions MCP Server - System Architecture

## Overview
The GrowMillions MCP (Model Context Protocol) Server provides a unified, secure, tool-driven interface connecting LLMs to internal microservices and external marketing platforms.

## Core Stack
- **Runtime**: Python 3.13
- **Server Framework**: FastAPI + FastMCP (`mcp.server.fastmcp`)
- **HTTP Client**: `httpx` (Async HTTP)
- **Data Validation**: Pydantic V2
- **Package Manager**: `uv`

## System Design & Layering