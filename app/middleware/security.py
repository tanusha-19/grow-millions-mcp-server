"""JWT Authentication and Scope Authorization Middleware."""
from typing import List, Optional
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.config.settings import settings

security_scheme = HTTPBearer(auto_error=False)
class IdentityContext(BaseModel):
    user_id: str
    tenant_id: str
    scopes: List[str] = Field(default_factory=list)

class SecurityMiddleware(BaseHTTPMiddleware):
    """HTTP Middleware for enforcing basic security headers."""

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response
def parse_identity_context(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security_scheme),
) -> IdentityContext:
    """Extracts and verifies JWT token from Bearer header."""
    if not credentials:
        if getattr(settings, "ENVIRONMENT", "development") == "development":
            return IdentityContext(
                user_id="dev-user-001",
                tenant_id="dev-tenant-growmillions",
                scopes=[
                    "business:read",
                    "strategy:read",
                    "content:generate",
                    "social:write",
                    "social:publish",
                    "ads:write",
                    "ads:publish",
                    "compliance:read",
                    "marketplace:read",
                ],
            )
        raise HTTPException(
            status_code=401, detail="Authentication credentials missing"
        )

    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[getattr(settings, "JWT_ALGORITHM", "HS256")],
            issuer=getattr(settings, "AUTH_ISSUER", "https://growmillions.in"),
        )
        return IdentityContext(
            user_id=payload.get("sub", "unknown"),
            tenant_id=payload.get("tenant_id", "default"),
            scopes=payload.get("scopes", []),
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid authorization token")
def check_scope(required_scope: str, identity: IdentityContext) -> None:
    """Validates if identity possesses the required permission scope."""
    if required_scope not in identity.scopes:
        raise HTTPException(
            status_code=403,
            detail=f"Permission Denied: Missing required scope '{required_scope}'",
        )