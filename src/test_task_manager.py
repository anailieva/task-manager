import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    
    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.add_task("Task 3")


if __name__ == '__main__':
    unittest.main()
