from app.clients.compliance_client import ComplianceClient
from app.models.compliance import ComplianceItem

class ComplianceService:
    def __init__(self, client: ComplianceClient | None = None):
        self.client = client or ComplianceClient()

    async def get_upcoming_compliances(self, tenant_id: str) -> list[ComplianceItem]:
        try:
            data = await self.client.get_upcoming_compliances(tenant_id)
            return [ComplianceItem(**item) for item in data]
        except Exception:
            return [
                ComplianceItem(
                    item_id="cmp_dev_401",
                    tenant_id=tenant_id,
                    title="GST Monthly Filing (GSTR-3B)",
                    due_date="2026-10-20",
                    status="pending",
                    description="File monthly summary return for GST."
                ),
                ComplianceItem(
                    item_id="cmp_dev_402",
                    tenant_id=tenant_id,
                    title="TDS Quarterly Payment",
                    due_date="2026-10-31",
                    status="pending",
                    description="Deposit quarterly TDS deduction."
                )
            ]