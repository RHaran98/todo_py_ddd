from shared.base_classes import ValueObject
from pydantic import Field


# Value object
# Mutable
# Non identifiable
class ToDoTask(ValueObject):
    task_description:   str = Field(max_length=200)
    is_completed:       bool = False

    # @validator("task_description",pre=True)
    # def validate_description(cls, value):
    #     if isinstance(ag)


