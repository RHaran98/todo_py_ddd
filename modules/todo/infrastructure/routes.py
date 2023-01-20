from fastapi import APIRouter
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.repository.d_implements.in_memory import InMemoryToDoRepo
from modules.todo.usecases.create_todo_task.create_todo_task import CreateTaskUseCaseImplement
from modules.todo.usecases.delete_todo_task.delete_todo_task import DeleteTaskUseCaseImplement
from modules.todo.usecases.get_todo_tasks.get_todo_tasks import GetTasksUseCaseImplement
from modules.todo.usecases.replace_todo_task.replace_todo_task import ReplaceTaskUseCaseImplement

inmemory_router = APIRouter()
todo_repo = InMemoryToDoRepo()


@inmemory_router.get("/todos", tags=["todo"])
def get_tasks():
    get_usecase = GetTasksUseCaseImplement(todo_repo)
    result = get_usecase.get_tasks()
    if result is not None:
        return result
    else:
        return {}


@inmemory_router.post("/todos", tags=["todo"])
def create_task(task: ToDoTask = ToDoTaskFactory.create_task("")):
    create_usecase = CreateTaskUseCaseImplement(todo_repo)
    result = create_usecase.create_task(task)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}


@inmemory_router.put("/todos/{id}", tags=["todo"])
def replace_task(
        id: int,
        task: ToDoTask = ToDoTaskFactory.create_task("")):
    replace_usecase = ReplaceTaskUseCaseImplement(todo_repo)
    result = replace_usecase.replace_task(id, task)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}


@inmemory_router.delete("/todos/{id}", tags=["todo"])
def delete_task(id: int):
    delete_usecase = DeleteTaskUseCaseImplement(todo_repo)
    result = delete_usecase.delete_task(id)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}
