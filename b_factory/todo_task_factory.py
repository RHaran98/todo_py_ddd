from typing import Union

from a_domains.todo_task import ToDoTask
from a_domains.todo_container import ToDoContainer
from pydantic import ValidationError
from typing import TypedDict


class ToDoTaskDict(TypedDict):
    task_description: str
    is_completed: bool


class ToDoTaskFactory:
    @staticmethod
    def create_task(task_description: str, is_completed: bool = False) -> Union[None, ToDoTask]:
        try:
            task = ToDoTask(task_description=task_description, is_completed=is_completed)
        except ValidationError:
            return None
        return task


class ToDoContainerFactory:
    @staticmethod
    def create_list(task_list: list[ToDoTaskDict]) -> Union[None, ToDoContainer]:
        try:
            todo_list = ToDoContainer(tasks=task_list)
        except ValidationError:
            return None
        return todo_list
