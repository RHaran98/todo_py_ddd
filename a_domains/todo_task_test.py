import unittest

from pydantic import ValidationError

from todo_task import ToDoTask


class ToDoTasksTestCase(unittest.TestCase):
    def test_task_generation(self):
        task = ToDoTask(task_description="Get milk", is_completed=False)

    def test_task_multiple_generation(self):
        task1 = ToDoTask(task_description="Task 1", is_completed=False)
        task2 = ToDoTask(task_description="Task 2", is_completed=False)
        self.assertEqual(task1.task_description, "Task 1")
        self.assertEqual(task2.task_description, "Task 2")

    def test_task_value(self):
        task = ToDoTask(task_description="Get milk", is_completed=False)
        self.assertEqual(task.task_description, "Get milk")
        self.assertEqual(task.is_completed, False)

    def test_task_completion_default(self):
        task = ToDoTask(task_description="Get milk")
        self.assertEqual(task.task_description, "Get milk")
        self.assertEqual(task.is_completed, False)

    def test_task_completion_set(self):
        task = ToDoTask(task_description="Get milk", is_completed=True)
        self.assertEqual(task.task_description, "Get milk")
        self.assertEqual(task.is_completed, True)

    def test_task_coercion(self):
        task = ToDoTask(task_description=1000, is_completed="true")
        self.assertEqual(task.task_description, "1000")
        self.assertEqual(task.is_completed, True)

    def test_task_description_length(self):
        ToDoTask(task_description="A"*1, is_completed="true")
        ToDoTask(task_description="A"*200, is_completed="true")
        self.assertRaises(ValidationError,ToDoTask,task_description="A"*201, is_completed="true")


if __name__ == '__main__':
    unittest.main()
