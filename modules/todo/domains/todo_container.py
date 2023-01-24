from typing import List
from pydantic import Field
from modules.todo.domains.todo_task import ToDoTask
from shared.base_classes import Entity
from uuid import uuid4


# Entity
# Identifiable
# Mutable (Preferably not)
class ToDoContainer(Entity):
    id: str = Field(default_factory=uuid4)
    tasks: List[ToDoTask] = []

