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

@app.get("/tasks",response_model=list[model.TaskResponse])
def get_all():
    return database.db_get_all_task()

@app.get("/tasks/{id}",response_model=model.TaskResponse)
def get_one(id:int):
    return database.db_get_one(id)