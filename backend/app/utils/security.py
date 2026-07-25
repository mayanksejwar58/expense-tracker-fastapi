import bcrypt

# bcrypt has a hard 72-byte limit on the input; truncate defensively so
# very long passwords don't raise instead of just being capped.
_MAX_BYTES = 72


def hash_password(password: str) -> str:
    truncated = password.encode("utf-8")[:_MAX_BYTES]
    hashed = bcrypt.hashpw(truncated, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password.encode("utf-8")[:_MAX_BYTES]
    try:
        return bcrypt.checkpw(truncated, hashed_password.encode("utf-8"))
    except ValueError:
        return False