from unittest import TestCase
from c_repository.d_implements.in_memory import InMemoryToDoRepo
from b_factory.todo_task_factory import ToDoTaskFactory
from a_domains.todo_container import ToDoContainer
from a_domains.todo_task import ToDoTask

class InMemoryToDoRepoTestcase(TestCase):

    def test_repo_creation(self):
        todo = InMemoryToDoRepo()
        self.assertIsInstance(todo.get_tasks(), ToDoContainer)
        self.assertEqual(len(todo.get_tasks().tasks), 0)

    def test_task_creation(self):
        todo = InMemoryToDoRepo()
        tasks = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)
        self.assertIsInstance(todo.get_tasks(), ToDoContainer)
        self.assertEqual(len(todo.get_tasks().tasks), 10)

    def test_task_deletion(self):
        todo = InMemoryToDoRepo()
        tasks = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)

        res = todo.delete_task(10)
        self.assertEqual(res, False)

        res = todo.delete_task(9)
        self.assertEqual(res, True)
        self.assertIsInstance(todo.get_tasks(), ToDoContainer)
        self.assertEqual(len(todo.get_tasks().tasks), 9)

    def test_task_replace(self):
        todo = InMemoryToDoRepo()
        tasks = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)

        res = todo.replace_task(10,ToDoTaskFactory.create_task("Special",is_completed=True))
        self.assertEqual(res, False)

        res = todo.replace_task(9, ToDoTaskFactory.create_task("Special", is_completed=True))
        self.assertEqual(res, True)
        test_task = todo.get_tasks().tasks[9]
        self.assertIsInstance(test_task, ToDoTask)
        self.assertEqual(test_task.task_description, "Special")
        self.assertEqual(test_task.is_completed, True)