from abc import ABC, abstractmethod
from a_domains.todo_task import ToDoTask
from c_repository.interface import ToDoRepo


class ReplaceTaskUseCase(ABC):
    @abstractmethod
    def replace_task(self, index: int, task: ToDoTask) -> bool:
        pass


class ReplaceTaskUseCaseImplement(ReplaceTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def replace_task(self, index: int, task: ToDoTask) -> bool:
        result = self.todo_repo.replace_task(index=index,task=task)
        return result
