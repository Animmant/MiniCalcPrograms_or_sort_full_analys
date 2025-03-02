import math

class TaskManager:
    def __init__(self):
        self.tasks = {
            "1": (self.task_1, 2),
            "3": (self.task_3, 0),
            "4": (self.task_4, 0),
            "11": (self.task_11, 2)
        }

    def execute_task(self, task_number, variables):
        if task_number not in self.tasks:
            return "Unknown Task"
        
        task_function, required_vars = self.tasks[task_number]
        if len(variables) < required_vars:
            remaining = required_vars - len(variables)
            return f"Waiting for {remaining} more input(s)... (Enter {remaining} value{'s' if remaining > 1 else ''})"
        
        try:
            description, input_data, result = task_function(variables)
            return f"{description}\nInput Data: {input_data}\nResult: {result}"
        except Exception as e:
            return f"Error during calculation: {str(e)}"

    def task_1(self, variables):
        x, y = variables if len(variables) == 2 else (1, 2)
        result = (1 + math.sin(x + y) ** 2) / (2 + abs((x - 2 * x) / (1 + x**2 * y**2))) + x
        return "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x", f"x = {x}, y = {y}", result

    def task_3(self, _):
        return "π * π", "π = 3.141592...", math.pi * math.pi

    def task_4(self, _):
        return "π^π", "π = 3.141592...", math.pi ** math.pi

    def task_11(self, variables):
        a, n = variables if len(variables) == 2 else (2, 3)
        result = sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))
        return "The sum 1/a + 1/a^2 + ... + 1/a^(2^n)", f"a = {a}, n = {n}", result
