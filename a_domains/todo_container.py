from typing import List
from a_domains.todo_task import ToDoTask
from shared.base_classes import Entity
from pydantic import BaseModel


# Entity
# Identifiable
# Mutable (Preferably not)
class ToDoContainer(Entity):
    tasks: List[ToDoTask]

    def __eq__(self, o: object) -> bool:
        if isinstance(o, ToDoContainer):
            if o.tasks == self.tasks and o.id == self.id:
                return True
            else:
                return False
        return False
