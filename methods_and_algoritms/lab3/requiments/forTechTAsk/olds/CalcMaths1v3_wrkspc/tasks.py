"""
Цей файл залишено для зворотної сумісності.
Він перенаправляє всі запити до нової структури пакету tasks.

УВАГА: Цей файл буде видалено в майбутніх версіях.
Оновіть свій код для використання нової структури.
"""

# Імпортуємо TaskManager з нового пакету
from tasks.task_manager import TaskManager

# Для зворотної сумісності з кодом, який використовує інші функції з цього файлу
from tasks import math_tasks, text_tasks

# Створюємо клас-обгортку, який перенаправляє до нового TaskManager 
class LegacyTaskManager(TaskManager):
    """
    Клас для зворотної сумісності.
    Всі звернення до цього класу будуть перенаправлені до нового TaskManager.
    """
    pass

# Заміщуємо клас TaskManager класом LegacyTaskManager для зворотної сумісності
TaskManager = LegacyTaskManager 