"""
TaskManager - центральний клас для управління задачами.

Відповідає за реєстрацію, виконання та обробку задач різних типів.
"""

from . import task_registry

class TaskManager:
    """
    Клас для управління та виконання задач.
    
    В новій архітектурі TaskManager більше не містить самі задачі,
    а лише керує їх реєстрацією та виконанням.
    """
    
    def __init__(self):
        """
        Ініціалізує TaskManager.
        
        TaskManager тепер використовує централізований реєстр задач
        замість зберігання їх безпосередньо.
        """
        # В новій архітектурі задачі не зберігаються безпосередньо в TaskManager
        self.tasks = task_registry.get_all_tasks()
    
    def register_task(self, task_id, task_function, required_vars, data_type):
        """
        Реєструє нову задачу в системі.
        
        Args:
            task_id (str): Унікальний ідентифікатор задачі
            task_function (callable): Функція, що виконує задачу
            required_vars (int): Кількість необхідних вхідних параметрів
            data_type (type): Тип даних для вхідних параметрів
        """
        task_registry.register_task(task_id, task_function, required_vars, data_type)
        self.tasks = task_registry.get_all_tasks()
    
    def execute_task(self, task_number, variables):
        """
        Виконує задачу за її номером з наданими змінними.
        
        Args:
            task_number (str): Ідентифікатор задачі
            variables (list): Список вхідних параметрів
            
        Returns:
            str: Результат виконання задачі або повідомлення про помилку
        """
        if task_number not in self.tasks:
            return "Unknown Task"
        
        task_function, required_vars, data_type = self.tasks[task_number]
        if len(variables) < required_vars:
            remaining = required_vars - len(variables)
            return f"Waiting for {remaining} more input(s)... (Enter {remaining} value{'s' if remaining > 1 else ''})"
        
        try:
            converted_variables = [data_type(var) for var in variables]
            description, input_data, result = task_function(converted_variables)
            return f"{description}\nInput Data: {input_data}\nResult: {result}"
        except Exception as e:
            return f"Error during calculation: {str(e)}" 