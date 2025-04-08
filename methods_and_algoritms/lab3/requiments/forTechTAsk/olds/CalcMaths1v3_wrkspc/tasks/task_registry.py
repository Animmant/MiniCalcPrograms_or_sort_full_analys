"""
Система реєстрації задач для проєкту CalcMaths.

Цей модуль забезпечує центральний механізм реєстрації та управління задачами.
"""

from . import math_tasks
from . import text_tasks

# Словник для зберігання зареєстрованих задач
# Формат: {"id_задачі": (функція, кількість_параметрів, тип_даних)}
_TASK_REGISTRY = {}

def register_task(task_id, task_function, required_vars, data_type):
    """
    Реєструє нову задачу в системі.
    
    Args:
        task_id (str): Унікальний ідентифікатор задачі
        task_function (callable): Функція, що виконує задачу
        required_vars (int): Кількість необхідних вхідних параметрів
        data_type (type): Тип даних для вхідних параметрів
    """
    _TASK_REGISTRY[task_id] = (task_function, required_vars, data_type)
    
def get_task(task_id):
    """
    Отримує задачу за її ідентифікатором.
    
    Args:
        task_id (str): Ідентифікатор задачі
        
    Returns:
        tuple: (функція, кількість_параметрів, тип_даних) або None, якщо задачу не знайдено
    """
    return _TASK_REGISTRY.get(task_id)

def get_all_tasks():
    """
    Повертає всі зареєстровані задачі.
    
    Returns:
        dict: Словник зареєстрованих задач
    """
    return _TASK_REGISTRY

def register_default_tasks():
    """
    Реєструє задачі за замовчуванням.
    
    Ця функція повинна викликатися під час ініціалізації пакету.
    """
    # Реєстрація математичних задач
    register_task("1", math_tasks.task_1, 2, float)
    register_task("2", math_tasks.task_2, 2, float)
    
    # Реєстрація текстових задач
    register_task("6.ayes", text_tasks.task_6_a, 1, str)
    register_task("18", text_tasks.task_18, 1, str)

# Автоматична реєстрація задач при імпорті модуля
register_default_tasks() 