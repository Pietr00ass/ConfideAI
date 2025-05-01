from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import CryptoRequest
from ..services.crypto import encrypt_file, decrypt_file
from ..dependencies import get_db

router = APIRouter()

@router.post('/encrypt')
def api_encrypt(req: CryptoRequest, db: Session = Depends(get_db)):
    try:
        out = encrypt_file(req.filepath, req.remove_original)
        return {"status": "encrypted", "path": out}
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post('/decrypt')
def api_decrypt(req: CryptoRequest, db: Session = Depends(get_db)):
    try:
        out = decrypt_file(req.filepath, req.remove_original)
        return {"status": "decrypted", "path": out}
    except Exception as e:
        raise HTTPException(400, str(e))
