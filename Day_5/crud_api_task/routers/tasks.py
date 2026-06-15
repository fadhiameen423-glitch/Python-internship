import fastapi
import schema
router=fastapi.APIRouter(prefix="/tasks",tags=["Tasks"])
tasks={}
next_id=1
@router.get("/",response_model=list[schema.TaskResponse])
def get_all():
    return list(tasks.values())

@router.get("/{id}",response_model=schema.TaskResponse)
def get_one(id: int):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    return tasks[id]

@router.post("/",response_model=schema.TaskResponse)
def create_task(task:schema.TaskCreate):
    global next_id
    new_task={
        "id":next_id,
        "title":task.title,
        "completed":False
    }
    tasks[next_id]=new_task
    next_id +=1
    return new_task

@router.put("/{id}",response_model=schema.TaskResponse)
def update(id:int,task:schema.TaskUpdate):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    tasks[id]={
        "id":id,
        "title":task.title,
        "completed":task.completed
    }
    return tasks[id]

@router.delete("/{id}")
def delete_task(id:int):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    del tasks[id]
    return "Task deleted"

@router.patch("/{id}",response_model=schema.TaskResponse)
def completed_task(id:int):
    if id not in tasks:
        raise fastapi.HTTPException(status_code=404,message="Task not found")
    tasks[id]["completed"]=True
    return tasks[id]
