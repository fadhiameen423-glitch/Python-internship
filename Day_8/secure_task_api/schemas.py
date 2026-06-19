from pydantic import BaseModel
from typing import Optional

class RegisterUser(BaseModel):
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes=True

class TokenResponse(BaseModel):
    token: str

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title:Optional[str] = None
    completed:Optional[bool]=None

class TaskResponse(BaseModel):
    id:int
    title:str
    completed:bool
    owner_email:str

    class Config:
        from_attributes=True

