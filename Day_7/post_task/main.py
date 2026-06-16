import fastapi
import database
import model

app=fastapi.FastAPI()

@app.on_event("startup")
def startup():
    database.init_db()

@app.post("/tasks")
def create_task(task:model.TaskCreate):
    return database.db_create_task(task.model_dump())