from app.services.marketing_strategist import MarketingStrategistService
from app.auth.identity import IdentityContext
from app.models.strategy import StrategyPlanRequest

strategist_service = MarketingStrategistService()

async def generate_marketing_strategy_tool(
    identity: IdentityContext, 
    duration_days: int = 30, 
    goals: list[str] | None = None
) -> dict:
    """Generate a multi-day marketing plan for the authenticated tenant."""
    if not identity.has_scope("marketing:write"):
        raise PermissionError("Insufficient scope: marketing:write required")
    
    request = StrategyPlanRequest(
        duration_days=duration_days,
        goals=goals or []
    )
    plan = await strategist_service.generate_strategy(identity.tenant_id, request)
    return plan.model_dump()