from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import auth, crypto, ocr

app = FastAPI(title="Cryptonet WebAPI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(crypto.router, prefix="/crypto", tags=["crypto"])
app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])

@app.get("/")
def read_root():
    return {"message": "Cryptonet API działa!"}
