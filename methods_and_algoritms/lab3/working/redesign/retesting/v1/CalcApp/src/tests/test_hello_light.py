# tests/test_hello.py
import unittest
from utils.hello import calculate_expression

# Створюємо клас для тестів, успадковуючись від unittest.TestCase
class TestHelloFunction(unittest.TestCase):

    # Метод тестування (назва повинна починатися з 'test_')
    def test_calculate_expression_returns_hello_world(self):
        """
        Перевіряє, чи функція calculate_expression повертає рядок 'hello world'.
        """
        # Очікуваний результат
        expected_result = "hello world"
        # Отримуємо фактичний результат від функції
        actual_result = calculate_expression()

        print(f"Очікували '{expected_result}', але отримали '{actual_result}'")
        # Використовуємо метод assertEqual для порівняння очікуваного та фактичного результатів
        self.assertEqual(expected_result, actual_result,
                         f"Очікували '{expected_result}', але отримали '{actual_result}'")

    def test_calculate_expression_returns_string(self):
        """
        Check that calculate_expression returns a string.
        """
        result = calculate_expression()
        self.assertIsInstance(result, str, "Function should return a string (str)")

# Цей блок дозволяє запускати тести безпосередньо з цього файлу
if __name__ == '__main__':
    unittest.main()