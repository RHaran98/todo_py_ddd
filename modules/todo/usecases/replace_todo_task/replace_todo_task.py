from abc import ABC, abstractmethod
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.repository.interface import ToDoRepo
from modules.todo.usecases.dto import ReplaceTaskDTO

class ReplaceTaskUseCase(ABC):
    @abstractmethod
    def replace_task(self, task_info: ReplaceTaskDTO) -> bool:
        pass


class ReplaceTaskUseCaseImplement(ReplaceTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def replace_task(self, task_info: ReplaceTaskDTO) -> bool:
        task = ToDoTaskFactory.create_task(task_description=task_info.task_description,
                                           is_completed=task_info.is_completed)

        result = self.todo_repo.replace_task(id=task_info.id, task=task)
        return result
