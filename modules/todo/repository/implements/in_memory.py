from modules.todo.domains.todo_container import ToDoContainer
from modules.todo.domains.todo_task import ToDoTask
from modules.todo.repository.interface import ToDoRepo
from modules.todo.factory.todo_task_factory import ToDoContainerFactory
from modules.todo.factory.todo_task_factory import ToDoTaskFactory


class InMemoryToDoRepo(ToDoRepo):
    def __init__(self):
        self._data: ToDoContainer = ToDoContainerFactory.create_list(task_list=[])

    def get_tasks(self) -> ToDoContainer:
        return self._data

    def create_task(self, task: ToDoTask) -> bool:
        try:
            self._data.tasks.append(task)
        except Exception as e:
            return False
        else:
            return True

    def delete_task(self, id: str) -> bool:
        ids = [t.id for t in self._data.tasks]

        if id in ids:
            index = ids.index(id)
            self._data.tasks.pop(index)
            return True
        else:
            return False

    def replace_task(self, id: str, task: ToDoTask) -> bool:
        ids = [t.id for t in self._data.tasks]

        if id in ids:
            index = ids.index(id)
            self._data.tasks[index].task_description = task.task_description
            self._data.tasks[index].is_completed = task.is_completed
            return True
        else:
            return False
