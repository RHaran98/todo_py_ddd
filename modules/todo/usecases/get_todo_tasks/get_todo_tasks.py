from abc import ABC, abstractmethod

from modules.todo.domains.todo_container import ToDoContainer
from modules.todo.repository.interface import ToDoRepo


class GetTasksUseCase(ABC):
    @abstractmethod
    def get_tasks(self) -> ToDoContainer:
        pass


class GetTasksUseCaseImplement(GetTasksUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def get_tasks(self) -> ToDoContainer:
        result = self.todo_repo.get_tasks()
        return result
