from passlib.context import CryptContext
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from fastapi import Depends,HTTPException
import uuid
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
sessions={}
security=HTTPBearer()
def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_session(email:str):
    token=str(uuid.uuid4())
    sessions[token]=email
    return token

def get_current_user(credentials:HTTPAuthorizationCredentials = Depends(security)):
    token=credentials.credentials
    if token not in sessions:
        raise HTTPException(status_code=401,detail="invalid token")
    return sessions[token]
