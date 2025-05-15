# src/components/math_tasks.py

from typing import List, Tuple, Callable, Optional
import math
import numpy
import matplotlib.pyplot as plt

Point = Tuple[float, float]
Points = List[Point]


def _calculate_divided_differences(points: Points) -> List[float]:
    """Обчислює та повертає список коефіцієнтів розділених різниць Ньютона [c₀, c₁, ...].
    cₖ = f[x₀, x₁, ..., xₖ]
    """
    n = len(points)
    if n < 2:
        raise ValueError("Потрібно щонайменше 2 точки для обчислення розділених різниць.")

    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    # Перевірка на унікальність X після перевірки кількості точок
    if len(set(x_coords)) != n:
        # Знаходимо дублікати для інформативного повідомлення
        seen = set()
        duplicates = {x for x in x_coords if x in seen or seen.add(x)}  # type: ignore
        raise ValueError(f"X-координати точок мають бути унікальними. Знайдено дублікати: {duplicates}")

    # 'coeffs' зберігає поточний стовпець обчислень. Починаємо з y-координат (0-й порядок різниць)
    coeffs = list(y_coords)
    # 'result_coeffs' буде зберігати фінальні коефіцієнти полінома [c₀, c₁, c₂, ...]
    result_coeffs = [coeffs[0]]  # c₀ = f[x₀] = y₀

    # Обчислюємо стовпці різниць від 1-го порядку до (n-1)-го
    for order in range(1, n):  # order - порядок різниці (1, 2, ..., n-1)
        next_coeffs = []  # Стовпець для різниць поточного порядку 'order'
        # Обчислюємо кожен елемент нового стовпця
        # Елемент j у стовпці 'order' обчислюється через елементи j та j+1 стовпця 'order-1'
        for j in range(n - order):  # j - індекс у *попередньому* стовпці (звідки беремо дані)
            denominator = x_coords[j + order] - x_coords[j]
            # Перевірка ділення на нуль або дуже близькі значення
            if math.isclose(denominator, 0.0, abs_tol=1e-12):  # Додано abs_tol для кращої стійкості
                raise ValueError(
                    f"Дуже близькі або однакові x-координати, що призводять до ділення на нуль "
                    f"при обчисленні різниці порядку {order}: "
                    f"x_{{j + order}}={x_coords[j + order]}, x_{{j}}={x_coords[j]}."  # Екрановано фігурні дужки
                )
            # Формула розділеної різниці: f[x_j, ..., x_{j+order}]
            diff = (coeffs[j + 1] - coeffs[j]) / denominator
            next_coeffs.append(diff)

        # Зберігаємо перший елемент нового стовпця - це наступний коефіцієнт полінома Ньютона
        result_coeffs.append(next_coeffs[0])  # c_order = f[x₀, x₁, ..., x_order]
        # Оновлюємо 'coeffs' для наступної ітерації (наступний стовпець стає поточним)
        coeffs = next_coeffs

    return result_coeffs


def _calculate_derivative_from_coeffs(coeffs: List[float], x_values: List[float], x0: float) -> float:
    """
    Обчислює похідну полінома Ньютона P'(x) в точці x0, де
    P(x) = c₀ + c₁(x-x₀) + c₂(x-x₀)(x-x₁) + ...
    P'(x) = c₁ + c₂[(x-x₀)+(x-x₁)] + c₃[(x-x₁)(x-x₂)+(x-x₀)(x-x₂)+(x-x₀)(x-x₁)] + ...

    Args:
        coeffs: Список коефіцієнтів розділених різниць [c₀, c₁, c₂, ...].
        x_values: Список x-координат [x₀, x₁, x₂, ...].
        x0: Точка, в якій обчислюється похідна.

    Returns:
        Наближене значення похідної в точці x0.
    """
    n = len(coeffs)
    if n < 2: return 0.0  # Похідна невизначена або константа 0 для однієї точки
    
    derivative = 0.0
    # c₁ - перший доданок похідної
    if n >= 2:
        derivative += coeffs[1]
        
    # Обчислення решти доданків: cᵢ * d/dx[Π_{j=0}^{i-1}(x-xⱼ)] evaluated at x0
    # d/dx [ Π_{j=0}^{i-1} (x-xⱼ) ] = Σ_{k=0}^{i-1} Π_{j=0, j!=k}^{i-1} (x-xⱼ)
    for i in range(2, n):  # Індекс коефіцієнта cᵢ (від c₂ до c_{n-1})
        term_derivative_sum = 0.0
        # Сума похідних добутків для поточного члена cᵢ
        for k in range(i):  # k - індекс множника (x-xₖ), який "виключається" при диференціюванні
            product = 1.0
            # Добуток Π (x0-xⱼ) для j від 0 до i-1, де j != k
            for j in range(i):
                if j == k:
                    continue
                product *= (x0 - x_values[j])
            term_derivative_sum += product
            
        # Додаємо внесок від члена cᵢ * (сума похідних добутків)
        derivative += coeffs[i] * term_derivative_sum
            
    return derivative


def approximate_derivative_newton(points: Points, x0: float) -> float:
    """
    Обчислює наближене значення першої похідної функції, заданої набором точок,
    в точці x0, використовуючи інтерполяційний поліном Ньютона.
    (Код залишається майже той самий, але тепер використовує правильну функцію похідної)
    """
    if not points:
        raise ValueError("Список точок не може бути порожнім.")
        
    x_values = [p[0] for p in points]

    # 1. Обчислити розділені різниці
    coeffs = _calculate_divided_differences(points)

    # 2. Обчислити похідну за загальною формулою
    derivative = _calculate_derivative_from_coeffs(coeffs, x_values, x0)

    return derivative


def _evaluate_newton_polynomial_and_derivative(coeffs: List[float], x_values: List[float], x: float) -> Tuple[float, float]:
    """
    Обчислює значення полінома Ньютона та його похідної в точці x.
    
    Args:
        coeffs: Список коефіцієнтів розділених різниць [c₀, c₁, c₂, ...].
        x_values: Список x-координат [x₀, x₁, x₂, ...].
        x: Точка, в якій обчислюється поліном та його похідна.
        
    Returns:
        Кортеж (значення полінома, значення похідної) в точці x.
    """
    if not coeffs:
        return 0.0, 0.0
        
    n = len(coeffs)
    
    # Базовий випадок для константного полінома
    if n == 1:
        return coeffs[0], 0.0
        
    # Загальний випадок
    polynomial_value = coeffs[0]
    derivative_value = 0.0
    
    # Обчислюємо значення полінома за схемою Горнера
    product = 1.0
    for i in range(1, n):
        product *= (x - x_values[i-1])
        polynomial_value += coeffs[i] * product
    
    # Обчислюємо похідну з використанням правила диференціювання
    for i in range(1, n):
        # Обчислюємо добуток (x-x₀)(x-x₁)...(x-xᵢ₋₁) для кожного i
        term = coeffs[i]
        # Обчислюємо похідну від (x-x₀)(x-x₁)...(x-xᵢ₋₁)
        derivative_term = 0.0
        
        for k in range(i):
            sub_product = 1.0
            for j in range(i):
                if j != k:
                    sub_product *= (x - x_values[j])
            derivative_term += sub_product
            
        derivative_value += term * derivative_term
    
    return polynomial_value, derivative_value


def plot_newton_interpolation(points: Points, num_points: int = 200, title: str = "Newton Interpolation and Derivative"):
    """
    Побудує графік полінома Ньютона та його похідної.
    """
    if not points:
        raise ValueError("Список точок для побудови графіку не може бути порожнім.")

    n = len(points)
    x_values_input = [p[0] for p in points]
    y_values_input = [p[1] for p in points]

    if n < 2:
        print("INFO: Недостатньо точок для побудови полінома або похідної (потрібно >= 2). Будуємо лише точки.")
        plt.figure(figsize=(10, 6))
        plt.plot(x_values_input, y_values_input, 'o', label="Data Points", color='red')  # Початкові точки
        plt.title(title)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.show()
        return
    
    # Обчислюємо коефіцієнти один раз
    coeffs = _calculate_divided_differences(points)

    # Визначаємо діапазон x для побудови графіку.
    # Розширюємо діапазон трохи за межі вхідних точок.
    min_x = min(x_values_input)
    max_x = max(x_values_input)
    plot_range_min = min_x - (max_x - min_x) * 0.1  # Розширюємо на 10%
    plot_range_max = max_x + (max_x - min_x) * 0.1  # Розширюємо на 10%
    
    if math.isclose(min_x, max_x):  # Якщо всі точки мають однакову X-координату (після перевірки на унікальність, це можливо лише для n=1?)
        # Але ми вже перевірили n < 2. Якщо n>=2 і x унікальні, такого не буде.
        # Проте, на всякий випадок, якщо діапазон нульовий, розширимо його фіксовано.
        if n > 0:  # Якщо є хоча б одна точка
            plot_range_min = min_x - 1.0
            plot_range_max = max_x + 1.0
        else:  # Порожній список вже оброблено на початку
            pass  # Should not reach here

    # Генеруємо x-значення для гладких ліній
    if num_points <= 1:
        plot_x_values = [plot_range_min] if n > 0 else []  # Малюємо одну точку, якщо є
    else:
        step = (plot_range_max - plot_range_min) / (num_points - 1)
        plot_x_values = [plot_range_min + i * step for i in range(num_points)]

    # Обчислюємо відповідні y-значення полінома та похідної
    plot_y_poly_values = []
    plot_y_deriv_values = []

    # Важливо: для обчислення полінома/похідної потрібен список x_values_input,
    # який відповідає коефіцієнтам coeffs
    
    for x_eval in plot_x_values:
        poly_val, deriv_val = _evaluate_newton_polynomial_and_derivative(coeffs, x_values_input, x_eval)
        plot_y_poly_values.append(poly_val)
        plot_y_deriv_values.append(deriv_val)

    # Будуємо графік
    plt.figure(figsize=(10, 6))  # Розмір фігури

    # Графік полінома
    plt.plot(plot_x_values, plot_y_poly_values, label="Newton Polynomial", color='blue')

    # Графік похідної
    if n >= 2:  # Похідна полінома 1-го ступеня (лінія) є константою. Для 0-го ступеня (точка) похідна 0 або невизначена.
        # Похідна має зміст, якщо є хоча б 2 точки (поліном >= 1 ступеня)
        plt.plot(plot_x_values, plot_y_deriv_values, label="Newton Polynomial Derivative", color='green', linestyle='--')

    # Початкові точки
    plt.plot(x_values_input, y_values_input, 'o', label="Data Points", color='red')

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()  # Додаємо легенду
    plt.grid(True)  # Додаємо сітку
    
    # Додаємо горизонтальну лінію на y=0 для кращого розуміння похідної
    plt.axhline(0, color='gray', lw=0.8)

    plt.show()  # Відображаємо графік
