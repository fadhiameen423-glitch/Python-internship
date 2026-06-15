import fastapi
squ=fastapi.FastAPI()
@squ.get("/square/{n}")
def get_square(n:int):
    return{"input":n,"result":n*n}