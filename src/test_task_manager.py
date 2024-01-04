import unittest
from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.add_task("Task 3")

    def test_add_task(self):
        self.task_manager.add_task("New Task")
        self.assertEqual(len(self.task_manager.tasks), 4)

    def test_mark_task_completed(self):
        self.task_manager.mark_task_completed(1)
        self.assertTrue(self.task_manager.tasks[1]["completed"])

        with self.assertRaises(IndexError):
            self.task_manager.mark_task_completed(5)

    def test_get_all_tasks(self):
        all_tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)
        self.assertEqual(all_tasks[0]["task"], "Task 1")
        self.assertFalse(all_tasks[1]["completed"])


if __name__ == '__main__':
    unittest.main()
