from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class LoginRequest(BaseModel):
    email:str
    password:str

@app.post("/auth/login")
def login(data:LoginRequest):
    if data.email=="user@example.com" and data.password=="password123":
        return{
            "access_token":"dummy_token123xyz",
            "email" : data.email
        }
    raise HTTPException(status_code=401,detail="Invalid email or password")
