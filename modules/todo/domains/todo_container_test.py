import unittest
from todo_container import ToDoContainer


class ContainerTestCase(unittest.TestCase):
    todo_list = ToDoContainer(tasks=[
        {
            "task_description": "Get some rest",
            "is_completed": True
        },
        {
            "task_description": "Get some milk",
            "is_completed": False
        },
        {
            "task_description": "Get some snacks",
        }
    ])

    def test_task_creation(self):
        self.assertEqual(ContainerTestCase.todo_list.tasks[0].task_description, "Get some rest")
        self.assertEqual(ContainerTestCase.todo_list.tasks[1].task_description, "Get some milk")
        self.assertEqual(ContainerTestCase.todo_list.tasks[2].task_description, "Get some snacks")

    def test_task_flags(self):
        self.assertEqual(ContainerTestCase.todo_list.tasks[0].is_completed, True)
        self.assertEqual(ContainerTestCase.todo_list.tasks[1].is_completed, False)
        self.assertEqual(ContainerTestCase.todo_list.tasks[2].is_completed, False)

    def test_list_length(self):
        self.assertEqual(len(ContainerTestCase.todo_list.tasks),3)

    def test_empty_list_allowed(self):
        empty_todo_list = ToDoContainer(tasks=[])
        self.assertEqual(len(empty_todo_list.tasks), 0)


if __name__ == '__main__':
    unittest.main()