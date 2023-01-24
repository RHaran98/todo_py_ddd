from abc import ABC, abstractmethod
from modules.todo.repository.interface import ToDoRepo
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.usecases.dto import CreateTaskDTO
class CreateTaskUseCase(ABC):
    @abstractmethod
    def create_task(self, task_info: CreateTaskDTO) -> bool:
        pass


class CreateTaskUseCaseImplement(CreateTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def create_task(self, task_info: CreateTaskDTO) -> bool:
        task = ToDoTaskFactory.create_task(task_description=task_info.task_description,
                                           is_completed=task_info.is_completed)
        result = self.todo_repo.create_task(task)
        return result

