from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt_handler import verify_token

# Shows a padlock + "Authorize" button in /docs and rejects requests
# with no/garbled Authorization header before we even see them.
bearer_scheme = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
) -> dict:
    """
    Dependency that validates the JWT on incoming requests.
    Use with: current_user: dict = Depends(get_current_user)
    Returns the token payload, e.g. {"sub": "<user_id>", "email": "...", "exp": ...}
    """

    token = credentials.credentials
    payload = verify_token(token)

    if payload is None or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

def get_current_user_id(
    current_user: dict = Depends(get_current_user)
) -> str:
    """Convenience dependency when a route only needs the user id."""
    return current_user["sub"]
