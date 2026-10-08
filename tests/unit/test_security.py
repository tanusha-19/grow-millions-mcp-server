from app.auth.identity import IdentityContext

def test_identity_context_has_scope():
    identity = IdentityContext(
        user_id="user_123",
        tenant_id="tenant_123",
        scopes=["business:read", "content:write"]
    )
    assert identity.has_scope("business:read") is True
    assert identity.has_scope("content:write") is True
    assert identity.has_scope("ads:publish") is False

def test_identity_context_wildcard_scope():
    identity = IdentityContext(
        user_id="admin_123",
        tenant_id="tenant_123",
        scopes=["*"]
    )
    assert identity.has_scope("business:read") is True
    assert identity.has_scope("any:permission") is True