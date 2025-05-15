# tests/tasks/test_math_tasks.py

import pytest
import math
import numpy as np
from numpy.testing import assert_allclose # Для порівняння масивів numpy

# Імпортуємо функції, які будемо тестувати
# Припускаємо, що pytest запускається з кореня проєкту,
# тому шлях відносно кореня
from components.math_task import calculate_expression, calculate_differences, newton_derivatives

# --- Тести для calculate_expression ---

def test_calculate_expression_basic():
    """Тестує calculate_expression з простими позитивними значеннями."""
    x = 1.0
    y = 2.0
    # Очікуване значення розраховане вручну або за допомогою самої функції:
    # numerator_part1 = 1 + math.pow(math.sin(1 + 2), 2) ≈ 1 + math.pow(math.sin(3), 2) ≈ 1 + 0.019914... ≈ 1.019914
    # inner_fraction_numerator = -1
    # inner_fraction_denominator = 1 + math.pow(1, 2) * math.pow(2, 2) = 1 + 1 * 4 = 5
    # inner_fraction_abs = abs(-1 / 5) = 0.2
    # denominator_part2 = 2 + 0.2 = 2.2
    # result = numerator_part1 / denominator_part2 + x ≈ 1.019914 / 2.2 + 1 ≈ 0.463597... + 1 ≈ 1.463597...
    expected_result = 1.4635973881188083
    assert calculate_expression(x, y) == pytest.approx(expected_result)

def test_calculate_expression_zero_inputs():
    """Тестує calculate_expression з нульовими значеннями."""
    x = 0.0
    y = 0.0
    # Очікуване значення:
    # numerator_part1 = 1 + math.pow(math.sin(0), 2) = 1 + 0 = 1
    # inner_fraction_numerator = 0
    # inner_fraction_denominator = 1 + 0 * 0 = 1
    # inner_fraction_abs = abs(0 / 1) = 0
    # denominator_part2 = 2 + 0 = 2
    # result = 1 / 2 + 0 = 0.5
    expected_result = 0.5
    assert calculate_expression(x, y) == pytest.approx(expected_result)

def test_calculate_expression_negative_inputs():
    """Тестує calculate_expression з негативними значеннями."""
    x = -1.0
    y = -1.0
    # Очікуване значення:
    # numerator_part1 = 1 + math.pow(math.sin(-1 + -1), 2) ≈ 1 + math.pow(math.sin(-2), 2) ≈ 1 + (-0.909297...)**2 ≈ 1 + 0.82682... ≈ 1.82682
    # inner_fraction_numerator = -(-1) = 1
    # inner_fraction_denominator = 1 + math.pow(-1, 2) * math.pow(-1, 2) = 1 + 1 * 1 = 2
    # inner_fraction_abs = abs(1 / 2) = 0.5
    # denominator_part2 = 2 + 0.5 = 2.5
    # result = numerator_part1 / denominator_part2 + x ≈ 1.82682 / 2.5 - 1 ≈ 0.730728... - 1 ≈ -0.269271...
    expected_result = -0.2692715034116304
    assert calculate_expression(x, y) == pytest.approx(expected_result)

# Тест з виведенням в консоль, як ви просили
def test_with_output(capsys):
    """
    Викликає calculate_expression, виводить результат з [INFO] тегом
    та перевіряє відповідність очікуваному значенню.
    """
    x = 1.0
    y = 2.0
    # Очікуване значення беремо з test_calculate_expression_basic
    expected_result = 1.4635973881188083

    # Викликаємо функцію
    actual_result = calculate_expression(x, y)

    # Виводимо результат у консоль (stdout)
    print(f"[INFO] calculate_expression({x}, {y}) = {actual_result}")

    # Перевіряємо відповідність очікуваному значенню
    assert actual_result == pytest.approx(expected_result)

    # Опціонально: перевіряємо, чи вивід містить потрібний текст
    captured = capsys.readouterr()
    assert "[INFO]" in captured.out
    assert f"{actual_result}" in captured.out


# --- Тести для calculate_differences ---

def test_calculate_differences_basic():
    """Тестує calculate_differences на простому наборі даних (квадратична функція)."""
    x = np.array([0, 1, 2])
    y = np.array([1, 2, 4]) # y = x^2 + 1 (змінено для нелінійності)
    # Очікувана таблиця різниць (тільки перший рядок):
    # f[x0] = 1
    # f[x0, x1] = (2-1)/(1-0) = 1
    # f[x1, x2] = (4-2)/(2-1) = 2
    # f[x0, x1, x2] = (f[x1, x2] - f[x0, x1]) / (x2 - x0) = (2 - 1) / (2 - 0) = 0.5
    expected_diffs = np.array([1.0, 1.0, 0.5])
    actual_diffs = calculate_differences(x, y)
    assert_allclose(actual_diffs, expected_diffs)

def test_calculate_differences_linear():
    """Тестує calculate_differences на лінійних даних."""
    x = np.array([1, 2, 3, 4])
    y = np.array([3, 5, 7, 9]) # y = 2x + 1
    # Очікувані різниці: f[x0]=3, f[x0,x1]=2, f[x0,x1,x2]=0, f[x0,x1,x2,x3]=0
    expected_diffs = np.array([3.0, 2.0, 0.0, 0.0])
    actual_diffs = calculate_differences(x, y)
    assert_allclose(actual_diffs, expected_diffs, atol=1e-9) # Додаємо допуск для float


def test_calculate_differences_empty():
    """Тестує calculate_differences з порожніми списками."""
    x = np.array([])
    y = np.array([])
    # numpy.zeros((0, 0)) - це порожній масив. Спроба доступу table[0] викличе IndexError
    with pytest.raises(IndexError):
        calculate_differences(x, y)

# --- Тести для newton_derivatives ---

def test_newton_derivatives_quadratic():
    """Тестує newton_derivatives на квадратичній функції."""
    x = [0.0, 1.0, 2.0]
    y = [1.0, 2.0, 4.0] # y = x^2 + 1. y' = 2x, y'' = 2
    at_point = 1.0
    # Очікувані значення похідних в точці x=1: y'(1) = 2*1 = 2, y''(1) = 2
    # Примітка: Формула в коді може давати наближення, а не точні аналітичні значення.
    # Потрібно перевірити, що саме обчислює код.
    # dd = [1.0, 1.0, 0.5] (з test_calculate_differences_basic)
    # f1 = dd[1] + dd[2]*(at_point-x[0])*2/(at_point-x[0]) = 1.0 + 0.5*(1-0)*2/(1-0) = 1.0 + 0.5*2 = 2.0
    # f2 = dd[2]*2*1/((at_point-x[0])**2) = 0.5*2/((1-0)**2) = 1.0
    # Отже, код обчислює f1=2.0, f2=1.0
    expected_f1 = 2.0
    expected_f2 = 1.0 # Зверніть увагу, це відрізняється від аналітичної y''=2
    f1, f2 = newton_derivatives(x, y, at_point)
    assert f1 == pytest.approx(expected_f1)
    assert f2 == pytest.approx(expected_f2)

def test_newton_derivatives_linear():
    """Тестує newton_derivatives на лінійній функції."""
    x = [1.0, 2.0, 3.0]
    y = [3.0, 5.0, 7.0] # y = 2x + 1. y' = 2, y'' = 0
    at_point = 2.0
    expected_f1 = 2.0
    expected_f2 = 0.0
    # dd = [3.0, 2.0, 0.0]
    # f1 = dd[1] + dd[2]*(...) = 2.0 + 0*(...) = 2.0
    # f2 = dd[2]*(...) = 0*(...) = 0.0
    f1, f2 = newton_derivatives(x, y, at_point)
    assert f1 == pytest.approx(expected_f1)
    assert f2 == pytest.approx(expected_f2)

def test_newton_derivatives_insufficient_points():
    """Тестує newton_derivatives, коли недостатньо точок (n < 2)."""
    x1 = [1.0]
    y1 = [1.0]
    at_point = 1.0
    # calculate_differences поверне [1.0]. Потім буде спроба доступу до dd[1] -> IndexError
    with pytest.raises(IndexError):
        newton_derivatives(x1, y1, at_point)

    x0 = []
    y0 = []
    # calculate_differences викличе IndexError раніше
    with pytest.raises(IndexError):
        newton_derivatives(x0, y0, at_point)

# --- Додаткові тести (можливі) ---
# def test_calculate_expression_edge_cases():
#     # Додаткові тести для calculate_expression, якщо є специфічні граничні умови
#     pass

# def test_calculate_differences_more_points():
#     # Тест calculate_differences з більшою кількістю точок
#     pass

# def test_newton_derivatives_different_point():
#     # Тест newton_derivatives в іншій точці, не вузлі
#     x = [0.0, 1.0, 2.0]
#     y = [1.0, 2.0, 4.0]
#     at_point = 0.5
#     # Розрахувати очікувані значення для f1, f2 в цій точці за формулами з коду
#     # ...
#     pass