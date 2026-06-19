from fastapi import APIRouter, HTTPException, Depends

import schemas
import auth
from database import get_db_connection

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=schemas.UserResponse)
def register(data: schemas.RegisterUser):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (data.email,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = auth.hash_password(data.password)

    cursor.execute(
        "INSERT INTO users (email, hashed_password) VALUES (?, ?)",
        (data.email, hashed_password),
    )
    conn.commit()

    new_user_id = cursor.lastrowid
    conn.close()

    return {"id": new_user_id, "email": data.email}


@router.post("/login", response_model=schemas.TokenResponse)
def login(data: schemas.LoginUser):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT hashed_password FROM users WHERE email = ?", (data.email,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not auth.verify_password(data.password, row["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_session(data.email)
    return {"token": token}


@router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user_email: str = Depends(auth.get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, email FROM users WHERE email = ?", (current_user_email,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": row["id"], "email": row["email"]}