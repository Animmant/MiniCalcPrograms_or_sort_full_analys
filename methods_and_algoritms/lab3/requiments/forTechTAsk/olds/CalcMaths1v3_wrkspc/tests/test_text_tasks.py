"""
Тести для текстових задач.
"""

import unittest
from tasks import text_tasks

class TestTextTasks(unittest.TestCase):
    """Тести для текстових функцій."""
    
    def test_text_split(self):
        """Тест для допоміжної функції розділення тексту на слова."""
        # Звичайний випадок
        result = text_tasks.text_split("hello world test")
        self.assertEqual(result, ["hello", "world", "test"])
        
        # Випадок з додатковими пробілами
        result = text_tasks.text_split("  hello   world  test  ")
        self.assertEqual(result, ["hello", "world", "test"])
        
        # Порожній рядок
        result = text_tasks.text_split("")
        self.assertEqual(result, [])
    
    def test_task_6_a(self):
        """Тест для задачі 6.a: Підрахунок пробілів до першого знаку оклику."""
        # Звичайний випадок
        description, input_data, result = text_tasks.task_6_a(["Hello world! How are you?"])
        self.assertEqual(result, 1)
        
        # Без пробілів до знаку оклику
        description, input_data, result = text_tasks.task_6_a(["Hello!"])
        self.assertEqual(result, 0)
        
        # Без знаку оклику
        description, input_data, result = text_tasks.task_6_a(["Hello world"])
        self.assertEqual(result, 0)
    
    def test_task_18(self):
        """Тест для задачі 18: Підрахунок слів з однаковими першим і останнім символами."""
        # Стандартний випадок
        description, input_data, result = text_tasks.task_18(["level deed stats"])
        self.assertIn("level", result)
        self.assertIn("deed", result)
        self.assertIn("stats", result)
        
        # Випадок з порожнім текстом
        description, input_data, result = text_tasks.task_18([""])
        self.assertIn("Count: 0", result)
        
        # Випадок без відповідних слів
        description, input_data, result = text_tasks.task_18(["hello world python"])
        self.assertIn("Count: 0", result)

if __name__ == '__main__':
    unittest.main() 