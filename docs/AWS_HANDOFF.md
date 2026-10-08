# AWS Infrastructure Deployment & Handoff Guide

## Overview
This document details the configuration and deployment handoff for hosting the Grow Millions MCP Server on AWS.

> **Prerequisite Note:** The Docker image still requires build and runtime verification in Aditya's environment before AWS deployment, as Docker Desktop was unavailable in the local development environment.

## Handoff Responsibilities
- **Development Scope (Tanusha):** Completed application logic, tool registration, security middleware, mock adapters, and 21/21 host-based unit/E2E tests.
- **Cloud & DevOps Scope (Aditya):** Container build verification, AWS ECR/ECS staging, domain configuration (`https://growmillions.in/mcp`), IAM policies, and live production release.

## Environment & Container Specifications
- **Base Image:** `python:3.11-slim-bookworm`
- **Package Manager:** `uv` (pinned version `0.5.11`)
- **Entry Point:** FastAPI / FastMCP server running on port `8000`
- **Healthcheck Endpoint:** `/health`
- **MCP Endpoint:** `/mcp`

## Deployment Checklist for AWS (Aditya)
1. [ ] Pull branch `feature/mcp-production-verification`
2. [ ] Build Docker image: `docker build -t grow-millions-mcp .`
3. [ ] Run containerized tests: `docker run --rm grow-millions-mcp uv run pytest`
4. [ ] Push container to AWS ECR
5. [ ] Provision ECS / App Runner service with SSL certificate for `growmillions.in`
6. [ ] Configure environment secrets (OAuth tokens, API keys) in AWS Secrets Manager
7. [ ] Verify `/health` and `/mcp` endpoints on staging URL