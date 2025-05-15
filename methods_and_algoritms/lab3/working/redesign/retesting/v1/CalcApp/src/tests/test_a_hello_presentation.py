import unittest
from src.utils.hello import calculate_expression

class TestHelloFunctionPresentation(unittest.TestCase):
    def test_output_for_presentation(self):
        """
        Демонстраційний тест для захисту лабораторної.
        Перевіряє, що функція повертає саме 'hello world',
        як доказ коректної роботи функції.
        """
        result = calculate_expression()
        print("\n[Демонстрація] Результат роботи функції:", result)
        self.assertEqual(result, "hello world")

if __name__ == '__main__':
    unittest.main()
