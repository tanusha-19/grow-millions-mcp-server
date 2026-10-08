"""Structured Audit Logging for GrowMillions MCP Server."""

import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, Optional

# Dedicated logger for audit events
audit_logger = logging.getLogger("mcp.audit")
audit_logger.setLevel(logging.INFO)

if not audit_logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    audit_logger.addHandler(handler)


def log_audit_event(
    tool_name: str,
    user_id: str,
    tenant_id: str,
    status: str,  # "SUCCESS", "DENIED", "FAILED"
    event_type: str = "mcp.tool.executed",
    payload_summary: Optional[Dict[str, Any]] = None,
    error_message: Optional[str] = None,
) -> None:
    """Logs structured audit events for high-risk write tools and compliance tracking."""
    audit_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "tool_name": tool_name,
        "user_id": user_id,
        "tenant_id": tenant_id,
        "status": status,
        "payload_summary": payload_summary or {},
        "error": error_message,
    }
    audit_logger.info(json.dumps(audit_record))