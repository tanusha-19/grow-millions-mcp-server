# API Contracts & Error Standards

## Error Format
All MCP tool error responses follow this standard structure:
```json
{
  "error": {
    "code": "AUTHORIZATION_ERROR | VALIDATION_ERROR | UPSTREAM_ERROR",
    "message": "Human readable description",
    "tenant_id": "tenant_xyz",
    "request_id": "req_123"
  }
}