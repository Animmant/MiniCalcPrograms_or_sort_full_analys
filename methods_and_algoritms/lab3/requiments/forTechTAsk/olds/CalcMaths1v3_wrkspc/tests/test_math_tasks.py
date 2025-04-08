"""
Тести для математичних задач.
"""

import unittest
from tasks import math_tasks

class TestMathTasks(unittest.TestCase):
    """Тести для математичних функцій."""
    
    def test_task_1(self):
        """Тест для задачі 1: Обчислення математичного виразу."""
        # Тестування зі звичайними значеннями
        description, input_data, result = math_tasks.task_1([2, 3])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        
        # Тестування з граничними значеннями
        description, input_data, result = math_tasks.task_1([0, 0])
        self.assertIsNotNone(result)
    
    def test_task_2(self):
        """Тест для задачі 2: Умовне присвоєння."""
        # Випадок x <= y (x стає 0)
        description, input_data, result = math_tasks.task_2([5, 10])
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 10)
        
        # Випадок x > y (x не змінюється)
        description, input_data, result = math_tasks.task_2([10, 5])
        self.assertEqual(result[0], 10)
        self.assertEqual(result[1], 5)

if __name__ == '__main__':
    unittest.main() 