from shared.base_classes import Entity
from pydantic import Field
from uuid import UUID, uuid4


# Value object
# Mutable
# Non identifiable
def create_uuid():
    return str(uuid4())
class ToDoTask(Entity):
    id: str = Field(default_factory=create_uuid)
    task_description: str = Field(max_length=200)
    is_completed: bool = False
