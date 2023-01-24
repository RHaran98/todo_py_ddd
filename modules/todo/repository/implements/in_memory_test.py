from unittest import TestCase
from modules.todo.repository.implements.in_memory import InMemoryToDoRepo
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.domains.todo_container import ToDoContainer
from modules.todo.domains.todo_task import ToDoTask

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
        tasks = [ToDoTaskFactory.create_task("Hello" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)

        id = "does_not_exist"
        res = todo.delete_task(id)
        self.assertEqual(res, False)

        id = todo._data.tasks[9].id
        res = todo.delete_task(id)
        self.assertEqual(res, True)
        self.assertIsInstance(todo.get_tasks(), ToDoContainer)
        self.assertEqual(len(todo.get_tasks().tasks), 9)

    def test_task_replace_not_found(self):
        todo = InMemoryToDoRepo()
        tasks = [ToDoTaskFactory.create_task("Hello" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)

        id = "does_not_exist"
        res = todo.replace_task(id, ToDoTaskFactory.create_task("Special",is_completed=True))
        self.assertEqual(res, False)

    def test_task_replace_found(self):
        todo = InMemoryToDoRepo()
        tasks = [ToDoTaskFactory.create_task("Hello" + str(i)) for i in range(10)]
        for task in tasks:
            todo.create_task(task)

        id = todo.get_tasks().tasks[9].id
        res = todo.replace_task(id, ToDoTaskFactory.create_task("Special", is_completed=True))
        self.assertEqual(res, True)
        test_task = todo.get_tasks().tasks[9]
        self.assertIsInstance(test_task, ToDoTask)
        self.assertEqual(test_task.task_description, "Special")
        self.assertEqual(test_task.is_completed, True)

