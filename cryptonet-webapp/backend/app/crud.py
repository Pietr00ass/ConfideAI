from sqlalchemy.orm import Session
from .models import User, OperationLog
import hashlib

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    db_user = User(username=username, password_hash=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def log_operation(db: Session, user_id: int, operation: str, detail: str):
    log = OperationLog(user_id=user_id, operation=operation, detail=detail)
    db.add(log)
    db.commit()
