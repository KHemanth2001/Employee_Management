from datetime import datetime, timedelta, UTC
from jose import jwt
from passlib.context import CryptContext
from app.config.env import settings
from app.config.constants import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hashes a plain-text password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    """Verifies a plain-text password against a hashed password."""
    return pwd_context.verify(password, hashed)


def create_access_token(data: dict) -> str:
    """Creates a JWT access token with an expiration time."""
    payload = data.copy()
    payload["exp"] = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token, secret_key, algorithms) -> dict:
    """Decodes and validates a JWT token."""
    return jwt.decode(token=token, key=secret_key, algorithms=algorithms)
