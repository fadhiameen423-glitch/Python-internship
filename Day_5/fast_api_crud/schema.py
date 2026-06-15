import pydantic


class Task(pydantic.BaseModel):
    title: str