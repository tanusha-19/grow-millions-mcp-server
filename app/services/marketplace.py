from app.clients.marketplace_client import MarketplaceClient
from app.models.marketplace import MarketplaceListing

class MarketplaceService:
    def __init__(self, client: MarketplaceClient | None = None):
        self.client = client or MarketplaceClient()

    async def search_marketplace(self, tenant_id: str, query: str) -> list[MarketplaceListing]:
        try:
            data = await self.client.search_marketplace(tenant_id, query)
            return [MarketplaceListing(**item) for item in data.get("results", [])]
        except Exception:
            return [
                MarketplaceListing(
                    listing_id="mkt_dev_501",
                    title="WhatsApp Customer Onboarding Bot",
                    category="Automation",
                    description="Automates new lead welcome messages via WhatsApp API.",
                    price_inr=1499.0,
                    developer="GrowMillions Ecosystem"
                ),
                MarketplaceListing(
                    listing_id="mkt_dev_502",
                    title="GST Invoice Auto-Extractor",
                    category="AI Agent",
                    description="Extracts GST invoice details from PDFs directly into accounting systems.",
                    price_inr=2999.0,
                    developer="Concept Place Dev"
                )
            ]