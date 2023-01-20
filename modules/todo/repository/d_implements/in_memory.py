from modules.todo.domains.todo_container import ToDoContainer
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.repository.interface import ToDoRepo
from modules.todo.factory.todo_task_factory import ToDoContainerFactory


class InMemoryToDoRepo(ToDoRepo):
    _data: ToDoContainer() = ToDoContainerFactory.create_list(task_list=[])

    def get_tasks(self) -> ToDoContainer:
        return self._data

    def create_task(self, task: ToDoTask) -> bool:
        data = self._data.dict()
        data["tasks"].append(task.dict())
        task_list = ToDoContainerFactory.create_list(task_list=data["tasks"])
        if task_list:
            self._data = task_list
            return True
        else:
            return False

    def delete_task(self, index: int) -> bool:
        data = self._data.dict()
        if index >= len(data["tasks"]):
            return False
        else:
            data["tasks"].pop(index)
            task_list = ToDoContainerFactory.create_list(task_list=data["tasks"])
            if task_list:
                self._data = task_list
                return True
            else:
                return False

    def replace_task(self, index: int, task: ToDoTask) -> bool:
        data = self._data.dict()
        if index >= len(data["tasks"]):
            return False
        else:
            data["tasks"][index] = task.dict()
            task_list = ToDoContainerFactory.create_list(task_list=data["tasks"])
            if task_list:
                self._data = task_list
                return True
            else:
                return False