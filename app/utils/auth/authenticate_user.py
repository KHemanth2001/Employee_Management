from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repository.users_repository import get_user
from app.utils.auth.jwt import decode_token
from app.config.env import settings

security = HTTPBearer()

def authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """
        Authenticates a user using a JWT bearer token.
        Validates the token, extracts the username, and verifies the user exists in the database.
    """
    try:
        payload = decode_token(token=credentials.credentials, secret_key=settings.SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")

        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

        user = get_user(db, username=username)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

        return user

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication credentials"
        )
