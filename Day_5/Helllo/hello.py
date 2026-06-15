import fastapi
hel=fastapi.FastAPI()
@hel.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}