"""
Пакет tasks — колекція математичних та текстових задач.

Цей пакет містить логіку для виконання різних обчислювальних та текстових задач,
організовану в модульну структуру.
"""

# Імпорт основних компонентів для зовнішнього використання
from .task_manager import TaskManager
from . import task_registry
from . import math_tasks
from . import text_tasks

# Реєстрація модулів та задач
__all__ = ['TaskManager', 'task_registry', 'math_tasks', 'text_tasks']

# Логування ініціалізації пакету
print("Initializing tasks package...")

# У майбутньому тут буде імпорт всіх необхідних класів та функцій 