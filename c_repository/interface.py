from abc import ABC, abstractmethod
from a_domains.todo_task import ToDoTask
from a_domains.todo_container import ToDoContainer


class ToDoRepo(ABC):
    @abstractmethod
    def get_tasks(self) -> ToDoContainer:
        pass

    @abstractmethod
    def create_task(self, task: ToDoTask) -> bool:
        pass

    @abstractmethod
    def delete_task(self, index: int) -> bool:
        pass

    @abstractmethod
    def replace_task(self, index: int, task: ToDoTask) -> bool:
        pass
