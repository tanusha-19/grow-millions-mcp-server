from app.services.compliance import ComplianceService
from app.auth.identity import IdentityContext

compliance_service = ComplianceService()

async def get_upcoming_compliances_tool(identity: IdentityContext) -> list[dict]:
    """Retrieve upcoming compliance obligations for the tenant."""
    if not identity.has_scope("compliance:read"):
        raise PermissionError("Insufficient scope: compliance:read required")

    items = await compliance_service.get_upcoming_compliances(identity.tenant_id)
    return [item.model_dump() for item in items]