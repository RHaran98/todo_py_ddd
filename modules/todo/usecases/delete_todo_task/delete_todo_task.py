from abc import ABC, abstractmethod
from modules.todo.repository.interface import ToDoRepo


class DeleteTaskUseCase(ABC):
    @abstractmethod
    def delete_task(self, index: int) -> bool:
        pass


class DeleteTaskUseCaseImplement(DeleteTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def delete_task(self, index: int) -> bool:
        result = self.todo_repo.delete_task(index)
        return result
