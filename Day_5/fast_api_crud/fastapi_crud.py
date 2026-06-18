import fastapi
import pydantic
app=fastapi.FastAPI()
tasks={}
next_id=1
class Task(pydantic.BaseModel):
    title:str

@app.get("/tasks")
def get_all():
    return list(tasks.values())

@app.get("/tasks/{id}")
def get_one(id:int):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    return tasks[id]

@app.post("/tasks")
def create_task(task:Task):
    global next_id
    new_task={
        "id":next_id,
        "title":task.title
    }
    tasks[next_id]=new_task
    next_id+=1
    return new_task

@app.put("/task/{id}")
def update_task(id:int,task:Task):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    tasks[id]["title"]=task.title
    return tasks[id]

@app.delete("/tasks/{id}")
def delete_task(id:int):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    del tasks[id]
    return "deleted task"
