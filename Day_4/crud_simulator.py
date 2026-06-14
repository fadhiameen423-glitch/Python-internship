import pydantic
tasks={}
task_id_counter=1
class Task(pydantic.BaseModel):
    title: str
    completed: bool = False

class TaskNotFound(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(f"{message}")

def create_task(data: dict) -> dict:
    global task_id_counter
    try:
        task=Task(**data)
    except pydantic.ValidationError as e:
        print("Validation error: ",e)
    tasks[task_id_counter]=task.model_dump()
    result={"id":task_id_counter,**tasks[task_id_counter]}
    task_id_counter+=1
    return result

def get_all_tasks() -> list:
    return[{"id":tid,**task}for tid,task in tasks.items()]

def get_task(id:int) -> dict:
    if id not in tasks:
        raise TaskNotFound(f"Task {id} not found")
    return{"id":id,**tasks[id]}

def update_task(task_id: int, data: dict)->dict:
    if task_id not in tasks:
        raise TaskNotFound(f"Task {task_id} not found")
    try:
        task = Task(**data)
    except pydantic.ValidationError as e:
        print("Validation Error:", e)
        return
    
    tasks[task_id] = task.model_dump()
    return {"id": task_id, **tasks[task_id]}

def delete_task(task_id: int)->bool:
    if task_id not in tasks:
        raise TaskNotFound(f"Task {task_id} not found")
    del tasks[task_id]
    return True

def menu():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                title = input("Enter title: ")
                print(create_task({"title": title}))

            elif choice == "2":
                print(get_all_tasks())

            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                print(get_task(task_id))

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                title = input("New title: ")
                completed = input("Completed (y/n): ") == "y"

                print(update_task(task_id, {
                    "title": title,
                    "completed": completed
                }))

            elif choice == "5":
                task_id = int(input("Enter task ID: "))
                delete_task(task_id)
                print("Task deleted successfully")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except TaskNotFound as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)
menu()