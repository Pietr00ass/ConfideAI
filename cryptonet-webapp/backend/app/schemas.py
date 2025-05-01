from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class CryptoRequest(BaseModel):
    filepath: str
    remove_original: bool = False
