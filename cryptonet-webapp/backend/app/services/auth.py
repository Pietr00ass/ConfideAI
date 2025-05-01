import jwt
import hashlib
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..config import settings
from ..crud import get_user_by_username, create_user

def register_user(username: str, password: str, db: Session):
    if get_user_by_username(db, username):
        raise HTTPException(400, "User exists")
    user = create_user(db, username, password)
    token = jwt.encode({"sub": user.username}, settings.jwt_secret, algorithm="HS256")
    return token

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db, username)
    if not user or user.password_hash != hashlib.sha256(password.encode()).hexdigest():
        raise HTTPException(401, "Invalid credentials")
    token = jwt.encode({"sub": user.username}, settings.jwt_secret, algorithm="HS256")
    return token
