import fastapi
import database
import routers.tasks

app = fastapi.FastAPI()


@app.on_event("startup")
def startup():
    database.init_db()


app.include_router(
    routers.tasks.router
)