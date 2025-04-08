"""
Математичні задачі проєкту CalcMaths.

Цей модуль містить реалізації різних математичних завдань.
"""

import math

def task_1(variables):
    """
    Задача 1: Обчислення математичного виразу.
    
    (1 + sin(x + y) ** 2) / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x
    
    Args:
        variables (list): Список змінних [x, y]
        
    Returns:
        tuple: (опис задачі, опис вхідних даних, результат)
    """
    x, y = variables if len(variables) == 2 else (1, 2)
    result = (1 + math.sin(x + y) ** 2) / (2 + abs((x - 2 * x) / (1 + x**2 * y**2))) + x
    return "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x", f"x = {x}, y = {y}", result

def task_2(variables):
    """
    Задача 2: Умовне присвоєння.
    
    Якщо x <= y, то x = 0, інакше x залишається без змін.
    
    Args:
        variables (list): Список змінних [x, y]
        
    Returns:
        tuple: (опис задачі, опис вхідних даних, результат)
    """
    x, y = variables if len(variables) == 2 else (1, 2)
    if x <= y:
        x = 0
    result = x, y
    return "x = 0 if x <= y else x, y", f"x = {x}, y = {y}", result

# Майбутні математичні задачі буде додано тут 