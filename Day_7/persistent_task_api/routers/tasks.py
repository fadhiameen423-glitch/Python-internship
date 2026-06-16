import fastapi
import schema
import database

router = fastapi.APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=list[schema.TaskResponse])
def get_all(status: str | None = None):

    if status:
        return database.db_search_tasks(status)

    return database.db_get_all_tasks()


@router.get("/{id}", response_model=schema.TaskResponse)
def get_one(id: int):

    task = database.db_get_task(id)

    if task is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.post("/")
def create_task(task: schema.TaskCreate):

    return database.db_create_task(
        task.model_dump()
    )


@router.put("/{id}", response_model=schema.TaskResponse)
def update(id: int, task: schema.TaskUpdate):

    updated = database.db_update_task(
        id,
        task.model_dump()
    )

    if updated is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@router.delete("/{id}")
def delete_task(id: int):

    deleted = database.db_delete_task(id)

    if not deleted:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted"}


@router.patch("/{id}",
              response_model=schema.TaskResponse)
def complete_task(id: int):

    task = database.db_complete_task(id)

    if task is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task