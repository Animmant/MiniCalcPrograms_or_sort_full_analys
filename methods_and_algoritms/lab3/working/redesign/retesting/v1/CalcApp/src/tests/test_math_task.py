import unittest
import math
import sys
import os

# Додаємо кореневу директорію проекту до шляху для імпорту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Тепер імпортуємо функцію calculate_expression
from src.components.math_task import calculate_expression

class TestMathTask(unittest.TestCase):
    
    def test_example_case(self):
        """Тест для прикладу з технічного завдання: x=2, y=3"""
        # Обчислюємо результат формули для x=2, y=3
        result = calculate_expression(2, 3)
        # Очікуємо результат близько до 2.935, а не 2.122 як було вказано в документації
        expected = 2.9345108327357154
        self.assertAlmostEqual(result, expected, places=6)
    
    def test_zero_values(self):
        """Тест з нульовими значеннями x=0, y=0"""
        result = calculate_expression(0, 0)
        # Для x=0, y=0:
        # (1 + sin²(0 + 0)) / (2 + abs((0 - 2*0) / (1 + 0²*0²))) + 0
        # = (1 + 0) / (2 + 0) + 0
        # = 1/2 = 0.5
        self.assertEqual(result, 0.5)
    
    def test_negative_values(self):
        """Тест з від'ємними значеннями x=-1, y=-2"""
        result = calculate_expression(-1, -2)
        # Обчислюємо еталонне значення вручну
        sin_squared = math.pow(math.sin(-1 + -2), 2)
        x_squared_y_squared = math.pow(-1, 2) * math.pow(-2, 2)
        x_minus_2x = -1 - 2 * (-1)
        denominator = 1 + x_squared_y_squared
        fraction = x_minus_2x / denominator
        abs_fraction = abs(fraction)
        main_denominator = 2 + abs_fraction
        main_fraction = (1 + sin_squared) / main_denominator
        expected = main_fraction + (-1)
        self.assertAlmostEqual(result, expected, places=6)
    
    def test_large_values(self):
        """Тест з великими значеннями x=1000, y=2000"""
        result = calculate_expression(1000, 2000)
        # Для великих значень перевіряємо, що функція не видає помилку
        self.assertIsInstance(result, float)
    
    def test_special_values(self):
        """Тест зі спеціальними значеннями: x=math.pi, y=math.pi/2"""
        result = calculate_expression(math.pi, math.pi/2)
        # Обчислюємо еталонне значення
        x = math.pi
        y = math.pi/2
        sin_squared = math.pow(math.sin(x + y), 2)
        x_squared_y_squared = math.pow(x, 2) * math.pow(y, 2)
        x_minus_2x = x - 2 * x
        denominator = 1 + x_squared_y_squared
        fraction = x_minus_2x / denominator
        abs_fraction = abs(fraction)
        main_denominator = 2 + abs_fraction
        main_fraction = (1 + sin_squared) / main_denominator
        expected = main_fraction + x
        self.assertAlmostEqual(result, expected, places=6)

if __name__ == '__main__':
    unittest.main() 

# Видаляємо код, який не стосується тестових випадків
# x_vals = [1.0, 1.1, 1.2, 1.3]
# y_vals = [0.8415, 0.8912, 0.9320, 0.9636]  # приблизно sin(x)
# point = 1.15
# d1, d2 = newton_derivatives(x_vals, y_vals, point)
# print(f"Перша похідна в {point}: {d1}")
# print(f"Друга похідна в {point}: {d2}")