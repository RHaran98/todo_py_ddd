from unittest import TestCase
from modules.todo.usecases.create_todo_task.create_todo_task import CreateTaskUseCaseImplement
from modules.todo.usecases.delete_todo_task.delete_todo_task import DeleteTaskUseCaseImplement
from modules.todo.usecases.get_todo_tasks.get_todo_tasks import GetTasksUseCaseImplement
from modules.todo.usecases.replace_todo_task.replace_todo_task import ReplaceTaskUseCaseImplement
from modules.todo.repository.d_implements.in_memory import InMemoryToDoRepo
from modules.todo.factory.todo_task_factory import ToDoTaskFactory
from modules.todo.domains.todo_container import ToDoContainer


# from domains.todo_task import ToDoTask

class InMemoryToDoRepoTestcase(TestCase):

    def test_create_usecase(self):
        fixtures = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        todo_repo = InMemoryToDoRepo()
        create_usecase = CreateTaskUseCaseImplement(todo_repo)
        for task in fixtures:
            create_usecase.create_task(task)
        self.assertEqual(len(todo_repo.get_tasks().tasks), 10)

    def test_delete_usecase(self):
        fixtures = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        todo_repo = InMemoryToDoRepo()
        for task in fixtures:
            todo_repo.create_task(task)

        delete_usecase = DeleteTaskUseCaseImplement(todo_repo)
        for i in range(10):
            delete_usecase.delete_task(0)
            self.assertEqual(len(todo_repo.get_tasks().tasks), 10 - (i + 1))

    def test_replace_usecase(self):
        fixtures = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        todo_repo = InMemoryToDoRepo()
        for task in fixtures:
            todo_repo.create_task(task)

        replace_usecase = ReplaceTaskUseCaseImplement(todo_repo)
        for i in range(10):
            new_task = ToDoTaskFactory.create_task("Replaced!", is_completed=True)
            replace_usecase.replace_task(i, new_task)
            self.assertEqual(todo_repo.get_tasks().tasks[0].task_description, "Replaced!")
            self.assertEqual(todo_repo.get_tasks().tasks[0].is_completed, True)

    def test_get_usecases(self):
        fixtures = [ToDoTaskFactory.create_task("Helllo" + str(i)) for i in range(10)]
        todo_repo = InMemoryToDoRepo()
        for task in fixtures:
            todo_repo.create_task(task)

        get_usecase = GetTasksUseCaseImplement(todo_repo)
        task_list = get_usecase.get_tasks()
        self.assertIsInstance(task_list, ToDoContainer)
        self.assertEqual(len(task_list.tasks), 10)

    def test_all_usecases(self):
        todo_repo = InMemoryToDoRepo()
        create_usecase = CreateTaskUseCaseImplement(todo_repo)
        delete_usecase = DeleteTaskUseCaseImplement(todo_repo)
        replace_usecase = ReplaceTaskUseCaseImplement(todo_repo)
        get_usecase = GetTasksUseCaseImplement(todo_repo)

        create_usecase.create_task(ToDoTaskFactory.create_task("Hello world!", is_completed=True))
        task_list = get_usecase.get_tasks()
        self.assertIsInstance(task_list, ToDoContainer)
        self.assertEqual(len(task_list.tasks), 1)
        self.assertEqual(task_list.tasks[0].task_description, "Hello world!")
        self.assertEqual(task_list.tasks[0].is_completed, True)

        replace_usecase.replace_task(0, ToDoTaskFactory.create_task("Hello sun!", is_completed=False))
        task_list = get_usecase.get_tasks()
        self.assertIsInstance(task_list, ToDoContainer)
        self.assertEqual(len(task_list.tasks), 1)
        self.assertEqual(task_list.tasks[0].task_description, "Hello sun!")
        self.assertEqual(task_list.tasks[0].is_completed, False)

        delete_usecase.delete_task(0)
        task_list = get_usecase.get_tasks()
        self.assertIsInstance(task_list, ToDoContainer)
        self.assertEqual(len(task_list.tasks), 0)
