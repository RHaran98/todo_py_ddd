from pydantic import BaseModel


class CreateTaskDTO(BaseModel):
    task_description: str
    is_completed: bool = False


class DeleteTaskDTO(BaseModel):
    id: str


class ReplaceTaskDTO(BaseModel):
    id: str
    task_description: str
    is_completed: bool = False

