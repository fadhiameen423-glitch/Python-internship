import pydantic
class TaskCreate(pydantic.BaseModel):
    title:str

class TaskUpdate(pydantic.BaseModel):
    title:str
    completed:bool

class TaskResponse(pydantic.BaseModel):
    id:int
    title:str
    completed:bool