from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError

from app.config.settings import settings


def create_access_token(data: dict) -> str:
    """Create a signed JWT. Expects data to include 'sub' (user id) and 'email'."""

    payload = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


def verify_token(token: str):
    """Decode and validate a JWT. Returns the payload dict, or None if invalid/expired."""

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload

    except JWTError:
        return None
