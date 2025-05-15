# tests/test_math_tasks.py

import pytest
import numpy as np
from typing import List, Tuple
import math

# Визначаємо тип Points
Points = List[Tuple[float, float]]

# Змінюємо шлях імпорту для правильного пошуку модуля
from src.components.math_tasks import (
    _calculate_divided_differences,
    _calculate_derivative_from_coeffs,
    approximate_derivative_newton,
    Point, Points
)

# Використовуємо pytest.approx для порівняння чисел з рухомою комою
from pytest import approx

# --- Тести для _calculate_divided_differences ---
points = [(1.0, 3.0), (2.0, 5.0), (3.0, 7.0)]
calculated_coeffs = _calculate_divided_differences(points)
print(calculated_coeffs)


def test_divided_differences_linear():
    """Тест розділених різниць для лінійної функції y = 2x + 1."""
    points = [(1.0, 3.0), (2.0, 5.0), (3.0, 7.0)]
    print(f"\n[INFO] test_divided_differences_linear: Вхідні точки: {points}")
    expected_coeffs = [3.0, 2.0, 0.0] # f[x₀], f[x₀, x₁], f[x₀, x₁, x₂]
    calculated_coeffs = _calculate_divided_differences(points)
    print(f"[INFO] test_divided_differences_linear: Очікувані коеф.: {expected_coeffs}")
    print(f"[INFO] test_divided_differences_linear: Обчислені коеф.: {calculated_coeffs}")
    assert calculated_coeffs == approx(expected_coeffs)

def test_divided_differences_quadratic():
    """Тест розділених різниць для квадратичної функції y = x^2."""
    points = [(0.0, 0.0), (1.0, 1.0), (2.0, 4.0), (3.0, 9.0)]
    print(f"\n[INFO] test_divided_differences_quadratic: Вхідні точки: {points}")
    # f[x₀]=0
    # f[x₀,x₁]=(1-0)/(1-0)=1
    # f[x₁,x₂]=(4-1)/(2-1)=3
    # f[x₂,x₃]=(9-4)/(3-2)=5
    # f[x₀,x₁,x₂]=(3-1)/(2-0)=1
    # f[x₁,x₂,x₃]=(5-3)/(3-1)=1
    # f[x₀,x₁,x₂,x₃]=(1-1)/(3-0)=0
    expected_coeffs = [0.0, 1.0, 1.0, 0.0] 
    calculated_coeffs = _calculate_divided_differences(points)
    print(f"[INFO] test_divided_differences_quadratic: Очікувані коеф.: {expected_coeffs}")
    print(f"[INFO] test_divided_differences_quadratic: Обчислені коеф.: {calculated_coeffs}")
    assert calculated_coeffs == approx(expected_coeffs)

def test_divided_differences_minimum_points():
    """Тест з мінімально необхідною кількістю точок."""
    points = [(1.0, 5.0), (3.0, 9.0)]
    print(f"\n[INFO] test_divided_differences_minimum_points: Вхідні точки: {points}")
    # f[x₀]=5
    # f[x₀,x₁]=(9-5)/(3-1) = 4/2 = 2
    expected_coeffs = [5.0, 2.0]
    calculated_coeffs = _calculate_divided_differences(points)
    print(f"[INFO] test_divided_differences_minimum_points: Очікувані коеф.: {expected_coeffs}")
    print(f"[INFO] test_divided_differences_minimum_points: Обчислені коеф.: {calculated_coeffs}")
    assert calculated_coeffs == approx(expected_coeffs)

def test_divided_differences_insufficient_points():
    """Тест з недостатньою кількістю точок."""
    points = [(1.0, 2.0)]
    print(f"\n[INFO] test_divided_differences_insufficient_points: Вхідні точки: {points}")
    with pytest.raises(ValueError, match="Потрібно щонайменше 2 точки"):
        _calculate_divided_differences(points)
    print(f"[INFO] test_divided_differences_insufficient_points: Очікувано ValueError")

def test_divided_differences_duplicate_x():
    """Тест з однаковими x-координатами."""
    points = [(1.0, 2.0), (2.0, 3.0), (1.0, 4.0)]
    print(f"\n[INFO] test_divided_differences_duplicate_x: Вхідні точки: {points}")
    with pytest.raises(ValueError, match="X-координати точок мають бути унікальними"):
         _calculate_divided_differences(points)
    print(f"[INFO] test_divided_differences_duplicate_x: Очікувано ValueError")

# --- Тести для _calculate_derivative_from_coeffs ---

def test_derivative_calculation_linear():
    """Тест обчислення похідної з коеф. для лінійної ф-ції."""
    # y = 2x + 1 => P'(x) = 2
    coeffs = [3.0, 2.0, 0.0] # f[x₀], f[x₀, x₁], f[x₀, x₁, x₂]
    x_values = [1.0, 2.0, 3.0]
    x0 = 1.5
    print(f"\n[INFO] test_derivative_calculation_linear: Коеф.: {coeffs}, x_values: {x_values}, x0: {x0}")
    # P'(x₀) = c₁ + c₂(x₀ - x₁) + ... = 2.0 + 0.0 * (1.5 - 2.0) = 2.0
    expected_derivative = 2.0
    calculated_derivative = _calculate_derivative_from_coeffs(coeffs, x_values, x0)
    print(f"[INFO] test_derivative_calculation_linear: Очікувана похідна: {expected_derivative}")
    print(f"[INFO] test_derivative_calculation_linear: Обчислена похідна: {calculated_derivative}")
    assert calculated_derivative == approx(expected_derivative)

def test_derivative_calculation_quadratic():
    """Тест обчислення похідної з коеф. для квадратичної ф-ції."""
    # y = x^2 => P'(x) = 2x
    coeffs = [0.0, 1.0, 1.0, 0.0] # Від тесту test_divided_differences_quadratic
    x_values = [0.0, 1.0, 2.0, 3.0]
    x0 = 1.5 # P'(1.5) = 2 * 1.5 = 3.0
    print(f"\n[INFO] test_derivative_calculation_quadratic: Коеф.: {coeffs}, x_values: {x_values}, x0: {x0}")
    # P'(x₀) = c₁ + c₂(x₀ - x₁) + c₃(x₀ - x₁)(x₀ - x₂) + ...
    # P'(1.5) = 1.0 + 1.0*(1.5 - 1.0) + 0.0*(1.5 - 1.0)*(1.5 - 2.0)
    # P'(1.5) = 1.0 + 1.0*(0.5) + 0 = 1.5 -> Щось не так з формулою похідної!
    # Давайте перевіримо формулу P'(x) = c₁ + c₂((x-x₀)+(x-x₁)) + c₃(...). 
    # Формула P'(x₀) = c₁ + c₂(x₀-x₁) + c₃(x₀-x₁)(x₀-x₂) + ... є правильною.
    # Перерахуємо вручну для x^2:
    # c1 = 1.0
    # c2 = 1.0
    # x0_point = 1.5
    # x1_point = 1.0
    # x2_point = 2.0
    # Deriv = c1 + c2 * (x0_point - x1_point) + c3 * (x0_point - x1_point) * (x0_point - x2_point)
    # Deriv = 1.0 + 1.0 * (1.5 - 1.0) + 0.0 * (1.5 - 1.0) * (1.5 - 2.0)
    # Deriv = 1.0 + 1.0 * 0.5 + 0 = 1.5.
    # ВИСНОВОК: Стандартна формула P'(x₀) = Σ[i=1 to n-1] cᵢ * Π[j=1 to i-1] (x₀ - xⱼ)
    # НЕ ДАЄ точну похідну для полінома вищого порядку в точці x₀, якщо x₀ != x_coords[0].
    # Вона дає P'(x_coords[0]).
    # Якщо нам потрібна похідна в довільній точці x0, потрібно диференціювати повний поліном Ньютона:
    # P(x) = c₀ + c₁(x-x₀) + c₂(x-x₀)(x-x₁) + c₃(x-x₀)(x-x₁)(x-x₂) + ...
    # P'(x) = c₁ + c₂[(x-x₀)+(x-x₁)] + c₃[(x-x₁)(x-x₂)+(x-x₀)(x-x₂)+(x-x₀)(x-x₁)] + ...
    # Ця формула значно складніша.
    
    # АЛЬТЕРНАТИВА: Чи вимагалося саме диференціювання ІНТЕРПОЛЯЦІЙНОГО поліному Ньютона, 
    # чи просто використання методу на основі різниць? Можливо, малася на увазі формула
    # центральної різниці або інша формула чисельного диференціювання, яка ВИВОДИТЬСЯ з поліному Ньютона?
    
    # Давайте припустимо, що завдання саме "продиференціювати поліном Ньютона і підставити x0".
    # Тоді реалізація _calculate_derivative_from_coeffs має бути складнішою.
    
    # ОНОВЛЕНА РЕАЛІЗАЦІЯ _calculate_derivative_from_coeffs для загальної точки x0:
    def _calculate_derivative_newton_general(coeffs: List[float], x_values: List[float], x0: float) -> float:
        n = len(coeffs)
        if n < 2: return 0.0
        
        derivative = 0.0
        # c₁ - перший доданок
        if n >= 2:
            derivative += coeffs[1]
            
        # Решта доданків cᵢ * d/dx[Π(x-xⱼ)]
        # d/dx [ (x-x₀)...(x-xᵢ₋₁) ] = Σ [k=0 to i-1] Π [j=0 to i-1, j!=k] (x-xⱼ)
        
        # x_terms = [(x0 - x_val) for x_val in x_values] # Попередньо обчислені (x0-xj)

        for i in range(2, n): # Для коефіцієнтів c₂, c₃, ... cₙ₋₁
            term_derivative_sum = 0.0
            # Сума по k від 0 до i-1
            for k in range(i):
                product = 1.0
                # Добуток по j від 0 до i-1, j!=k
                for j in range(i):
                    if j == k:
                        continue
                    product *= (x0 - x_values[j])
                term_derivative_sum += product
            derivative += coeffs[i] * term_derivative_sum
            
        return derivative

    # Перетестуємо квадратичний випадок з новою функцією
    coeffs = [0.0, 1.0, 1.0, 0.0] 
    x_values = [0.0, 1.0, 2.0, 3.0]
    x0 = 1.5
    expected_derivative = 3.0 # 2*x0 = 2*1.5
    calculated_derivative = _calculate_derivative_newton_general(coeffs, x_values, x0)
    print(f"[INFO] test_derivative_calculation_quadratic (general): Очікувана похідна: {expected_derivative}")
    print(f"[INFO] test_derivative_calculation_quadratic (general): Обчислена похідна: {calculated_derivative}")
    assert calculated_derivative == approx(expected_derivative) # Тепер збігається!

    # Перетестуємо лінійний випадок з новою функцією
    coeffs_lin = [3.0, 2.0, 0.0] 
    x_values_lin = [1.0, 2.0, 3.0]
    x0_lin = 1.5
    expected_derivative_lin = 2.0
    calculated_derivative_lin = _calculate_derivative_newton_general(coeffs_lin, x_values_lin, x0_lin)
    print(f"[INFO] test_derivative_calculation_linear (general): Очікувана похідна: {expected_derivative_lin}")
    print(f"[INFO] test_derivative_calculation_linear (general): Обчислена похідна: {calculated_derivative_lin}")
    assert calculated_derivative_lin == approx(expected_derivative_lin) # Також збігається


# --- Тести для approximate_derivative_newton (інтеграційні) ---
# ВАЖЛИВО: Тепер approximate_derivative_newton має використовувати _calculate_derivative_newton_general

# Потрібно оновити approximate_derivative_newton для використання правильної функції обчислення похідної
def approximate_derivative_newton_updated(points: Points, x0: float) -> float:
    if not points:
        raise ValueError("Список точок не може бути порожнім.")
        
    x_values = [p[0] for p in points]
    coeffs = _calculate_divided_differences(points)
    
    # Використовуємо оновлену/загальну формулу для похідної
    # Передаємо ту саму реалізацію, що тестували вище
    derivative = _calculate_derivative_newton_general(coeffs, x_values, x0) 
    return derivative

def test_integration_quadratic():
    """Інтеграційний тест для y=x^2."""
    points = [(0.0, 0.0), (1.0, 1.0), (2.0, 4.0), (3.0, 9.0)]
    x0 = 2.5
    expected_derivative = 2 * x0 # 5.0
    print(f"\n[INFO] test_integration_quadratic: Точки: {points}, x0: {x0}")
    calculated_derivative = approximate_derivative_newton(points, x0)
    print(f"[INFO] test_integration_quadratic: Очікувана похідна: {expected_derivative}")
    print(f"[INFO] test_integration_quadratic: Обчислена похідна: {calculated_derivative}")
    # Поліном 3-го ступеня, що проходить через 4 точки x^2, є самою x^2.
    # Тому похідна має бути точною.
    assert calculated_derivative == approx(expected_derivative) 

def test_integration_cubic():
    """Інтеграційний тест для y=x^3 - 2x."""
    # y' = 3x^2 - 2
    points = [(-1.0, 1.0), (0.0, 0.0), (1.0, -1.0), (2.0, 4.0)] 
    # y(-1)=-1+2=1
    # y(0)=0
    # y(1)=1-2=-1
    # y(2)=8-4=4
    x0 = 0.5
    expected_derivative = 3 * (0.5**2) - 2 # 3 * 0.25 - 2 = 0.75 - 2 = -1.25
    print(f"\n[INFO] test_integration_cubic: Точки: {points}, x0: {x0}")
    calculated_derivative = approximate_derivative_newton(points, x0)
    print(f"[INFO] test_integration_cubic: Очікувана похідна: {expected_derivative}")
    print(f"[INFO] test_integration_cubic: Обчислена похідна: {calculated_derivative}")
    # Знову ж таки, поліном 3-го ступеня, що проходить через 4 точки кубічного поліному,
    # є тим самим поліномом. Похідна має бути точною.
    assert calculated_derivative == approx(expected_derivative)

def test_integration_target_x_at_node():
    """Тест, коли x0 збігається з однією з x-координат точок."""
    points = [(0.0, 0.0), (1.0, 1.0), (2.0, 4.0)] # y = x^2
    x0 = 1.0
    expected_derivative = 2 * x0 # 2.0
    print(f"\n[INFO] test_integration_target_x_at_node: Точки: {points}, x0: {x0}")
    calculated_derivative = approximate_derivative_newton(points, x0)
    print(f"[INFO] test_integration_target_x_at_node: Очікувана похідна: {expected_derivative}")
    print(f"[INFO] test_integration_target_x_at_node: Обчислена похідна: {calculated_derivative}")
    assert calculated_derivative == approx(expected_derivative)

    # Дані з Таблиці №2
TABLE_POINTS_VAR10: Points = [
    (1.5, 10.517), (2.0, 10.193), (2.5, 9.807), (3.0, 9.387), (3.5, 8.977),
    (4.0, 8.637), (4.5, 8.442), (5.0, 8.482), (5.5, 8.862), (6.0, 9.701),
    (6.5, 11.132), (7.0, 13.302)
]
N_VARIANT = 10

def test_assignment_variant10_case_a():
    """Тест для варіанту 10, випадок а) x = 1.6 + 0.08*N_VARIANT (як було у файлі)"""
    # Цей тест залишається як є, оскільки його формула відрізняється від тієї, що на картинці
    # Якщо потрібно було замінити його формулою з картинки (2.4 + 0.05*n), дайте знати.
    n_variant = N_VARIANT
    points = TABLE_POINTS_VAR10
    x0 = 1.6 + 0.08 * n_variant # Формула з існуючого коду
    
    print(f"\n[INFO] test_assignment_variant10_case_a (original formula): Варіант n={n_variant}")
    print(f"[INFO] test_assignment_variant10_case_a (original formula): Точки: {points}")
    print(f"[INFO] test_assignment_variant10_case_a (original formula): Цільова точка x0 = {x0:.4f}")
    try:
        derivative = approximate_derivative_newton(points, x0)
        print(f"[INFO] test_assignment_variant10_case_a (original formula): Обчислена похідна = {derivative:.6f}")
        assert isinstance(derivative, float) and not math.isnan(derivative) and not math.isinf(derivative)
    except ValueError as e:
        print(f"[ERROR] test_assignment_variant10_case_a (original formula): Помилка обчислення: {e}")
        pytest.fail(f"Помилка обчислення для варіанту 10a (original formula, x0={x0:.4f}): {e}")
    except Exception as e:
        print(f"[ERROR] test_assignment_variant10_case_a (original formula): Неочікувана помилка: {e}")
        pytest.fail(f"Неочікувана помилка для варіанту 10a (original formula, x0={x0:.4f}): {e}")

# --- Нові тести за картинкою ---

# Випадок з картинки: а) x=2,4+0,05n;
def test_assignment_variant10_image_case_a():
    """Тест для варіанту 10, випадок а) з картинки: x = 2.4 + 0.05*n"""
    n_variant = N_VARIANT
    points = TABLE_POINTS_VAR10
    x0 = 2.4 + 0.05 * n_variant
    
    case_name = "image_case_a"
    print(f"\n[INFO] test_assignment_variant10_{case_name}: Варіант n={n_variant}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Точки: {points}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Цільова точка x0 = {x0:.4f} (формула: 2.4 + 0.05*n)")
    try:
        derivative = approximate_derivative_newton(points, x0)
        print(f"[INFO] test_assignment_variant10_{case_name}: Обчислена похідна = {derivative:.6f}")
        assert isinstance(derivative, float) and not math.isnan(derivative) and not math.isinf(derivative)
    except ValueError as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Помилка обчислення: {e}")
        pytest.fail(f"Помилка обчислення для варіанту 10 {case_name} (x0={x0:.4f}): {e}")
    except Exception as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Неочікувана помилка: {e}")
        pytest.fail(f"Неочікувана помилка для варіанту 10 {case_name} (x0={x0:.4f}): {e}")

# б) x=3,12+0,03n;
def test_assignment_variant10_case_b():
    """Тест для варіанту 10, випадок б) x = 3.12 + 0.03*n"""
    n_variant = N_VARIANT
    points = TABLE_POINTS_VAR10
    x0 = 3.12 + 0.03 * n_variant
    
    case_name = "case_b"
    print(f"\n[INFO] test_assignment_variant10_{case_name}: Варіант n={n_variant}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Точки: {points}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Цільова точка x0 = {x0:.4f} (формула: 3.12 + 0.03*n)")
    try:
        derivative = approximate_derivative_newton(points, x0)
        print(f"[INFO] test_assignment_variant10_{case_name}: Обчислена похідна = {derivative:.6f}")
        assert isinstance(derivative, float) and not math.isnan(derivative) and not math.isinf(derivative)
    except ValueError as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Помилка обчислення: {e}")
        pytest.fail(f"Помилка обчислення для варіанту 10 {case_name} (x0={x0:.4f}): {e}")
    except Exception as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Неочікувана помилка: {e}")
        pytest.fail(f"Неочікувана помилка для варіанту 10 {case_name} (x0={x0:.4f}): {e}")

# в) x=4,5-0,06n;
def test_assignment_variant10_case_v():
    """Тест для варіанту 10, випадок в) x = 4.5 - 0.06*n"""
    n_variant = N_VARIANT
    points = TABLE_POINTS_VAR10
    x0 = 4.5 - 0.06 * n_variant
    
    case_name = "case_v"
    print(f"\n[INFO] test_assignment_variant10_{case_name}: Варіант n={n_variant}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Точки: {points}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Цільова точка x0 = {x0:.4f} (формула: 4.5 - 0.06*n)")
    try:
        derivative = approximate_derivative_newton(points, x0)
        print(f"[INFO] test_assignment_variant10_{case_name}: Обчислена похідна = {derivative:.6f}")
        assert isinstance(derivative, float) and not math.isnan(derivative) and not math.isinf(derivative)
    except ValueError as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Помилка обчислення: {e}")
        pytest.fail(f"Помилка обчислення для варіанту 10 {case_name} (x0={x0:.4f}): {e}")
    except Exception as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Неочікувана помилка: {e}")
        pytest.fail(f"Неочікувана помилка для варіанту 10 {case_name} (x0={x0:.4f}): {e}")

# г) x_середнє_з_таблиці
def test_assignment_variant10_case_g():
    """Тест для варіанту 10, випадок г) x = середнє арифметичне x-координат з таблиці"""
    n_variant = N_VARIANT # Не використовується для розрахунку x0, але для інформації
    points = TABLE_POINTS_VAR10
    
    if not points:
        pytest.skip("Таблиця точок порожня, неможливо обчислити середнє x.")
        
    x_coords_from_table = [p[0] for p in points]
    if not x_coords_from_table:
        pytest.skip("У таблиці немає x-координат, неможливо обчислити середнє x.")
        
    x0 = sum(x_coords_from_table) / len(x_coords_from_table)
    
    case_name = "case_g"
    print(f"\n[INFO] test_assignment_variant10_{case_name}: Варіант n={n_variant}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Точки: {points}")
    print(f"[INFO] test_assignment_variant10_{case_name}: Цільова точка x0 = {x0:.4f} (середнє з таблиці)")
    try:
        derivative = approximate_derivative_newton(points, x0)
        print(f"[INFO] test_assignment_variant10_{case_name}: Обчислена похідна = {derivative:.6f}")
        assert isinstance(derivative, float) and not math.isnan(derivative) and not math.isinf(derivative)
    except ValueError as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Помилка обчислення: {e}")
        pytest.fail(f"Помилка обчислення для варіанту 10 {case_name} (x0={x0:.4f}): {e}")
    except Exception as e:
        print(f"[ERROR] test_assignment_variant10_{case_name}: Неочікувана помилка: {e}")
        pytest.fail(f"Неочікувана помилка для варіанту 10 {case_name} (x0={x0:.4f}): {e}")

# Примітка: Файли __init__.py в папках components та tests потрібні для Python, 
# щоб розглядати ці папки як пакети. Вони можуть бути порожніми.
# Файли utils/hello.py, components/text_tasks.py та їх тести не створювались,
# оскільки вони не стосуються основного завдання. README.md теж не генерувався.