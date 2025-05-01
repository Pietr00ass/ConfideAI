from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import UserCreate, Token
from ..services.auth import register_user, authenticate_user
from ..dependencies import get_db

router = APIRouter()

@router.post('/register', response_model=Token)
def register(data: UserCreate, db: Session = Depends(get_db)):
    token = register_user(data.username, data.password, db)
    return {"access_token": token}

@router.post('/login', response_model=Token)
def login(data: UserCreate, db: Session = Depends(get_db)):
    token = authenticate_user(data.username, data.password, db)
    return {"access_token": token}
