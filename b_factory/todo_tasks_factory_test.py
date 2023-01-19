import unittest
from todo_task_factory import ToDoTaskFactory, ToDoContainerFactory
from a_domains.todo_container import ToDoContainer
from a_domains.todo_task import ToDoTask


class ContainerTestCase(unittest.TestCase):
    def test_task_creation(self):
        task = ToDoTaskFactory.create_task(task_description="Hello world",is_completed=True)
        self.assertIsInstance(task, ToDoTask)
        self.assertEqual(task.task_description, "Hello world")
        self.assertEqual(task.is_completed, True)

    def test_task_creation_failure(self):
        task = ToDoTaskFactory.create_task(task_description="A"*201, is_completed=True)
        self.assertEqual(task, None)

    def test_task_container_creation(self):
        todo_list = ToDoContainerFactory.create_list([
            {
                "task_description":"Hello world",
                "is_completed":True
            },
            {
                "task_description": "Bye world",
                "is_completed": False
            }
        ])
        self.assertIsInstance(todo_list, ToDoContainer)

    # noinspection PyTypeChecker
    def test_task_container_creation_failure(self):
        todo_list = ToDoContainerFactory.create_list({"task_description":"Hello","is_completed":True})
        self.assertEqual(todo_list, None)


if __name__ == '__main__':
    unittest.main()