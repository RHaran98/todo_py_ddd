from abc import ABC, abstractmethod
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.repository.interface import ToDoRepo


class CreateTaskUseCase(ABC):
    @abstractmethod
    def create_task(self, task: ToDoTask) -> bool:
        pass


class CreateTaskUseCaseImplement(CreateTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def create_task(self, task: ToDoTask) -> bool:
        result = self.todo_repo.create_task(task)
        return result

