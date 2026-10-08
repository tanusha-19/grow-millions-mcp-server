# AWS Staging Deployment Guide

## Architecture
- **Compute:** AWS Lambda (arm64/x86_64 architecture)
- **Runtime Interface:** AWS Lambda Web Adapter (port 8080)
- **Ingress:** API Gateway HTTP API / HTTPS endpoint
- **Security:** AWS Secrets Manager for environment variables, IAM least-privilege execution role.

## Staging Deployment Steps (Pending Cloud Credentials)
1. Build container image for Lambda:
   ```bash
   docker build --platform linux/arm64 -t grow-millions-mcp-staging .