# AWS Infrastructure Handoff

## Overview
This document outlines the operational and configuration requirements for deploying the Grow Millions MCP Server package onto AWS Lambda via container image and API Gateway.

## Environment & Configuration
- **Runtime:** Python 3.11-slim-bookworm (retained for robust package compatibility and stability)
- **Dependency Manager:** `uv 0.5.11` (pinned)
- **Container Port:** 8080 (serves FastAPI and FastMCP via AWS Lambda Web Adapter `0.8.4`)
- **Health Endpoint:** `GET /health`
- **MCP Endpoint:** `POST /mcp` (or SSE transport as configured)

## Required Environment Variables (Managed via AWS Secrets Manager)
- `APP_ENV=production`
- `MCP_SERVER_NAME=grow-millions`
- `MCP_SERVER_VERSION=0.1.0`
- Upstream Service URLs (MARK-AI, Strategist, Content, Auto Post, Meta Ads, Compliance, Marketplace)
- Authentication Issuer & Audience (`AUTH_ISSUER`, `AUTH_AUDIENCE`)

## IAM Permissions & Roles
- **Execution Role:** Least-privilege Lambda execution role.
- **Secrets Manager:** `secretsmanager:GetSecretValue` permission for retrieving runtime configuration secrets.
- **CloudWatch:** Standard `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents`.

## Network & Ingress
- **Ingress:** API Gateway HTTP API with regional or edge-optimized payload routing.
- **Security Groups:** Restrict outbound calls where necessary; inbound HTTP/HTTPS traffic accepted via API Gateway.