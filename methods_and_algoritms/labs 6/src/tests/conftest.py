"""
Конфігураційний файл для pytest.
Він автоматично завантажується при запуску тестів.
"""
import os
import sys

# Додаємо батьківську директорію (src) до шляху Python
# Це потрібно, щоб модулі з src були доступні для імпорту у тестах
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir) 


    '''
    
    import numpy as np

def divided_difference(x_values, y_values):
    """
    Обчислює розділені різниці для заданих x та y значень.

    Args:
        x_values (list): Список x-координат вузлів.
        y_values (list): Список y-значень функції у вузлах.

    Returns:
        numpy.ndarray: Масив розділених різниць.
    """
    y = np.array(y_values, dtype=float)
    for i in range(1, len(x_values)):
        for j in range(len(x_values) - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x_values[j] - x_values[j - i])
    return y

def approximate_derivatives(x_values, y_values, x):
    """
    Обчислює наближені значення першої та другої похідних функції в точці x за допомогою методу Ньютона.

    Args:
        x_values (list): Список x-координат вузлів.
        y_values (list): Список y-значень функції у вузлах.
        x (float): Точка, в якій потрібно обчислити похідні.

    Returns:
        tuple: Кортеж з наближеними значеннями першої та другої похідних.
    """
    diffs = divided_difference(x_values, y_values)
    n = len(x_values)
    first_derivative = 0.0
    second_derivative = 0.0

    # Обчислення першої похідної
    for i in range(1, n):
        term = diffs[i]
        for j in range(i):
            term *= (x - x_values[j])
        first_derivative += term

    # Обчислення другої похідної
    for i in range(2, n):
        term = diffs[i]
        for j in range(i):
            term *= (x - x_values[j])
        # Приблизне обчислення другої похідної
        for j in range(i):
            for k in range(i):
                if j != k:
                    second_derivative += term / ((x - x_values[j]) - (x - x_values[k]))
    return first_derivative, second_derivative
    
    
    
    
    '''