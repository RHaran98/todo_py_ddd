from abc import ABC, abstractmethod
from modules.todo.repository.interface import ToDoRepo
from modules.todo.usecases.dto import DeleteTaskDTO

class DeleteTaskUseCase(ABC):
    @abstractmethod
    def delete_task(self, task_info: DeleteTaskDTO) -> bool:
        pass


class DeleteTaskUseCaseImplement(DeleteTaskUseCase):
    def __init__(self, todo_repo: ToDoRepo):
        self.todo_repo = todo_repo

    def delete_task(self, task_info: DeleteTaskDTO) -> bool:
        result = self.todo_repo.delete_task(task_info.id)
        return result
