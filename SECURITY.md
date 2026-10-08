# GrowMillions MCP Server - Security Architecture

## Security Principles
1. **Zero-Trust Tool Execution**: Every tool request validates identity and permissions.
2. **Read/Write Scope Separation**: Distinct scopes separate read/drafting actions from execution actions that impact state or finances.
3. **Auditability**: All write/publish activities trigger structured audit event logs.

## Scope Permission Matrix

| Tool Endpoint | Required Scope | Risk Level |
| :--- | :--- | :--- |
| `get_business_profile` | `business:read` | Low |
| `get_marketing_strategy` | `strategy:read` | Low |
| `generate_marketing_strategy` | `strategy:read` | Low |
| `generate_content` | `content:generate` | Low |
| `create_post_draft` | `social:write` | Medium |
| `schedule_post` | `social:publish` | **High** |
| `create_campaign_draft` | `ads:write` | Medium |
| `publish_campaign` | `ads:publish` | **High (Financial)** |
| `get_upcoming_compliances` | `compliance:read` | Low |
| `search_marketplace` | `marketplace:read` | Low |

## Authentication Flow
1. Client sends Bearer Token containing `sub` (User ID), `tenant_id`, and `scopes` list.
2. `SecurityMiddleware` verifies token against `JWT_SECRET_KEY` and expected `AUTH_ISSUER`.
3. `check_scope()` evaluates whether the user profile possesses the required permission.

## Audit Event Schema (`mcp.audit`)
All high-risk executions (`ads:publish`, `social:publish`) emit JSON audit logs containing:
- `timestamp`: UTC ISO format
- `tool_name`: Invoked tool identifier
- `user_id` & `tenant_id`: Context identity
- `status`: `SUCCESS`, `DENIED`, or `FAILED`
- `payload_summary`: Target parameters (e.g., `campaign_id`)