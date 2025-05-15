# tests/test_hello.py

import pytest
import numpy as np
import math # Імпортуємо math для порівняння з numpy.pi за потреби

# Імпортуємо напряму з каталогу utils
from utils.hello import calculate_expression, calc_area_of_circle

# --- Допоміжна функція (еквівалент методу _with_output) ---
def run_and_check_with_log(func, expected_value, *args, **kwargs):
    """
    Викликає функцію `func` з аргументами `*args`, `**kwargs`,
    друкує інформаційне повідомлення про виклик та результат,
    а потім перевіряє, чи результат відповідає `expected_value`.

    Args:
        func: Функція для тестування.
        expected_value: Очікуване значення, яке має повернути функція.
        *args: Позиційні аргументи для передачі у `func`.
        **kwargs: Іменовані аргументи для передачі у `func`.

    Returns:
        Фактичний результат виконання функції `func`.

    Raises:
        AssertionError: Якщо фактичний результат не відповідає очікуваному.
    """
    func_name = func.__name__
    arg_str = ", ".join(map(str, args))
    kwarg_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    call_signature = f"{func_name}({arg_str}{', ' if args and kwargs else ''}{kwarg_str})"

    print(f"\n[INFO] Calling: {call_signature}") # \n для кращої читабельності при запуску з -s

    actual_value = func(*args, **kwargs)

    print(f"[INFO] Function {func_name} returned: {actual_value}")
    print(f"[INFO] Expected value: {expected_value}")

    # Використовуємо pytest.approx для порівняння чисел з плаваючою комою
    if isinstance(expected_value, float) or (hasattr(np, 'floating') and isinstance(expected_value, np.floating)):
        print(f"[INFO] Asserting: {actual_value} approx == {expected_value}")
        assert actual_value == pytest.approx(expected_value)
    else:
        print(f"[INFO] Asserting: {actual_value} == {expected_value}")
        assert actual_value == expected_value

    print(f"[INFO] Assertion PASSED for {call_signature}")
    return actual_value

# --- Тести для calculate_expression ---

print(f"[INFO] Function {calculate_expression} expected: {'hello world'}")

def test_calculate_expression_basic():
    """Базова перевірка функції calculate_expression"""
    # Очікуване значення визначено прямо з коду функції
    expected = "hello world"
    actual = calculate_expression()
    assert actual == expected 

def test_calculate_expression_with_log():
    """Перевірка calculate_expression з використанням логування"""
    # Очікуване значення беремо з самої функції
    expected = calculate_expression() # Можна і так, якщо функція проста/детермінована
    run_and_check_with_log(calculate_expression, expected)
    # Або явно:
    # run_and_check_with_log(calculate_expression, "hello world")


# --- Тести для calc_area_of_circle ---

def test_calc_area_of_circle_basic():
    """Базова перевірка функції calc_area_of_circle"""
    radius = 2.0
    # Очікуване значення обчислюємо згідно з логікою функції
    expected = np.pi * (radius ** 2)
    actual = calc_area_of_circle(radius)
    # Використовуємо pytest.approx для порівняння float
    assert actual == pytest.approx(expected)

def test_calc_area_of_circle_zero_radius():
    """Перевірка calc_area_of_circle з нульовим радіусом"""
    radius = 0.0
    expected = 0.0 # np.pi * 0**2 = 0
    actual = calc_area_of_circle(radius)
    assert actual == pytest.approx(expected)

# Використання parametrize для тестування кількох випадків
@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (1.0, np.pi),          # Радіус 1
        (0.0, 0.0),          # Нульовий радіус
        (5.0, np.pi * 25.0), # Інший радіус
        (1 / np.sqrt(np.pi), 1.0) # Радіус, що дає площу 1
    ]
)

def test_calc_area_of_circle_parametrized(radius, expected_area):
    """Параметризований тест для calc_area_of_circle"""
    print(f"\n[DEBUG] Testing with radius = {radius}") # Додатковий вивід для демонстрації
    actual_area = calc_area_of_circle(radius)
    assert actual_area == pytest.approx(expected_area)


def test_calc_area_of_circle_with_log():
    """Перевірка calc_area_of_circle з використанням логування"""
    radius = 3.0
    # Очікуване значення обчислюємо згідно з логікою функції
    expected = np.pi * (radius ** 2)
    run_and_check_with_log(calc_area_of_circle, expected, radius)

def test_calc_area_of_circle_zero_radius_with_log():
    """Перевірка calc_area_of_circle з нульовим радіусом та логуванням"""
    radius = 0.0
    expected = 0.0
    run_and_check_with_log(calc_area_of_circle, expected, radius)

# Можна також параметризувати тести, що використовують логування
@pytest.mark.parametrize(
    "radius", [1.0, 10.0, np.sqrt(2)]
)
def test_calc_area_of_circle_parametrized_with_log(radius):
    """Параметризований тест для calc_area_of_circle з логуванням"""
    expected = np.pi * (radius ** 2)
    run_and_check_with_log(calc_area_of_circle, expected, radius)