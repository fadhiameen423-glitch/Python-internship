class HTTPError(Exception):
    def __init__(self,status_code,message):
        self.status_code=status_code
        self.message=message
        super().__init__(f"{status_code}:{message}")

def get_or_404(collection: dict, id: int) -> dict:
    if id not in collection:
        raise HTTPError(404,"Item not found")
    return collection[id]

tasks={
    1:{"title" : "Study"},
    2:{"title" : "Buy milk"},
    3:{"title":"Gym"}
}
print("\nValid id")
try:
    print(get_or_404(tasks,1))
except HTTPError as e:
    print(f"Error {e.status_code}: {e.message}")

print("\nInvalid id")
try:
    print(get_or_404(tasks,100))
except HTTPError as e:
    print(f"Error {e.status_code}: {e.message}")