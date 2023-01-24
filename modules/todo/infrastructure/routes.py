from fastapi import APIRouter, Path
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.repository.implements.in_memory import InMemoryToDoRepo
from modules.todo.usecases.create_todo_task.create_todo_task import CreateTaskUseCaseImplement
from modules.todo.usecases.delete_todo_task.delete_todo_task import DeleteTaskUseCaseImplement
from modules.todo.usecases.get_todo_tasks.get_todo_tasks import GetTasksUseCaseImplement
from modules.todo.usecases.replace_todo_task.replace_todo_task import ReplaceTaskUseCaseImplement
from modules.todo.usecases.dto import CreateTaskDTO, DeleteTaskDTO, ReplaceTaskDTO
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
def create_task(task_info: CreateTaskDTO):
    create_usecase = CreateTaskUseCaseImplement(todo_repo)
    result = create_usecase.create_task(task_info)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}


@inmemory_router.delete("/todos/{id}", tags=["todo"])
def delete_task(id: str):
    delete_usecase = DeleteTaskUseCaseImplement(todo_repo)
    delete_dto = DeleteTaskDTO(id=id)
    result = delete_usecase.delete_task(delete_dto)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}


@inmemory_router.put("/todos/{id}", tags=["todo"])
def replace_task(
        task: CreateTaskDTO,
        id: str = Path(title="Id of task"),
        ):

    replace_usecase = ReplaceTaskUseCaseImplement(todo_repo)
    replace_dto = ReplaceTaskDTO(id=id, task_description=task.task_description, is_completed=task.is_completed)
    result = replace_usecase.replace_task(replace_dto)
    if result is True:
        return {"status": "success"}
    else:
        return {"status": "failure"}
