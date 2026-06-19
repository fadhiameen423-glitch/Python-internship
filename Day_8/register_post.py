import sqlite3
from fastapi import FastAPI,HTTPException,Depends,Header
from pydantic import BaseModel
from passlib.context import CryptContext
import uuid

app=FastAPI()
pwd_context=CryptContext(schemes=["bcrypt"])
sessions={}

class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email:str
    password:str

conn=sqlite3.connect("app.db")
cursor=conn.cursor()
cursor.execute("create table if not exists users (id integer primary key autoincrement, email text unique, hashed_password text)")
conn.commit()
conn.close()

@app.post("/auth/register")
def register(data: RegisterRequest):
    conn=sqlite3.connect("app.db")
    cursor=conn.cursor()
    cursor.execute("select id from users where email=?",(data.email,))
    existing_user=cursor.fetchone()
    if existing_user:
        conn.close()
        raise HTTPException(status_code=400,detail="email already registered")
    hashed_password=pwd_context.hash(data.password)
    cursor.execute("insert into users(email,hashed_password) values (?,?)",(data.email,hashed_password))
    conn.commit()
    conn.close()
    return {"message":"User registered"}

@app.post("/auth/login")
def login(data:LoginRequest):
    conn=sqlite3.connect("app.db")
    cursor=conn.cursor()
    cursor.execute("select hashed_password from users where email=?",(data.email,))
    row=cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=401,detail="invalid credentials")
    hashed_password=row[0]
    if not pwd_context.verify(data.password,hashed_password):
        raise HTTPException(status_code=401,detail="invalid credentials")
    token=str(uuid.uuid4())
    sessions[token]=data.email
    return {"token":token}

def get_current_user(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid token format"
        )
    token = authorization.replace(
        "Bearer ",
        ""
    )
    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return sessions[token]

@app.get("/tasks")
def get_tasks(current_user=Depends(get_current_user)):
    return [
        {
            "id":1,
            "title":"Play Football"
        },
        {
            "id":2,
            "title":"Study python"
        }
    ]

@app.get("/")
def home():
    return {"message":"Home"}