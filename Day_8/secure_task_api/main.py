import time
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers import auth_router, tasks_router

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Task API")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI(title=APP_NAME)

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = time.time() - start_time

    print(f"{request.method} {request.url.path} - {response.status_code} - {duration_ms}ms")

    return response

app.include_router(auth_router.router)
app.include_router(tasks_router.router)

@app.get("/")
def home():
    return {"message": f"{APP_NAME} is running"}