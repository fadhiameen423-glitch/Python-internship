import fastapi
import schema

app = fastapi.FastAPI()

tasks = {}
next_id = 1


@app.post("/tasks")
def create_task(task: schema.Task):
    global next_id

    tasks[next_id] = {
        "id": next_id,
        "title": task.title
    }

    next_id += 1
    return tasks[next_id - 1]


@app.get("/tasks")
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]

    return {
        "message": "Task deleted"
    }