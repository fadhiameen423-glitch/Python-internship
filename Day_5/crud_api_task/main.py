import fastapi
import routers.tasks
app=fastapi.FastAPI()
app.include_router(routers.tasks.router)
