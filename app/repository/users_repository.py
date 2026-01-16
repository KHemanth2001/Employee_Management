from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User


def get_user(session: Session, user_id: Optional[str] = None, username: Optional[str] = None) -> User | None:
    query = session.query(User)
    if user_id:
        query = query.filter(User.id == user_id)

    if username:
        query = query.filter(User.username == username)

    return query.first()


