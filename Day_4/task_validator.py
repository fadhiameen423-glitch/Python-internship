import pydantic
class TaskModel(pydantic.BaseModel):
    title: str
    priority: str ="low"
    completed: bool = False

print("\nValid Task")
task=TaskModel(title="Buy Milk",priority="high",completed=True)
print(task)
print(task.model_dump())

print("\nInvalid Task")
try:
    bad_task=TaskModel(title=123)
except pydantic.ValidationError:
    print("Validation Error...")