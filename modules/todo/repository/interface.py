from abc import ABC, abstractmethod
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.domains.todo_container import ToDoContainer


class ToDoRepo(ABC):
    @abstractmethod
    def get_tasks(self) -> ToDoContainer:
        pass

    @abstractmethod
    def create_task(self, task: ToDoTask) -> bool:
        pass

    @abstractmethod
    def delete_task(self, id: str) -> bool:
        pass

    @abstractmethod
    def replace_task(self, id: str, task: ToDoTask) -> bool:
        pass
