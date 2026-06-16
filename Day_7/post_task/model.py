import pydantic

class TaskCreate(pydantic.BaseModel):
    title: str
    completed: bool = False

class TaskResponse(TaskCreate):
    id: int