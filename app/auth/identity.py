from pydantic import BaseModel, Field

class IdentityContext(BaseModel):
    user_id: str
    tenant_id: str
    scopes: list[str] = Field(default_factory=list)

    def has_scope(self, required_scope: str) -> bool:
        """Check if identity context has the required permission scope."""
        return required_scope in self.scopes or "*" in self.scopes