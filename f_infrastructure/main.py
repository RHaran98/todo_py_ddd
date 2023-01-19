from f_infrastructure.routes import inmemory_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(inmemory_router, prefix="/in_mem")


@app.get("/")
def root_handler():
    return "Welcome to the todo app"
