import math

"""
TASK_DEFINITIONS = {
    "1": ("task_1", 2, float, "Example: x = 1, y = 2"),
    "2": ("task_2", 2, float, "Example: x = 3, y = 5"),
    "3.1": ("task_3_1", 2, float, "Example: a = 2, n = 3"),
    "3.2": ("task_3_2", 2, float, "Example: a = 2, n = 4"),
    "4": ("task_4", 0, float, "Example: No input required"),
    "5": ("task_5", 0, float, "Example: No input required"),
    "6.a": ("task_6_a", 1, str, "Example: Hello world! How are you!"),
    "15": ("task_15", 1, str, "Example: Hello, world. 3 times, 3 more"),
    "18": ("task_18", 1, str, "Example: Hello   world  python   code")  
}
"""

class TaskManager:
    def __init__(self):
        self.tasks = {
            "1": (self.task_1, 2, float),
            "2": (self.task_2, 2, float),
            "3.1": (self.task_3_1, 2, float),
            "3.2": (self.task_3_2, 2, float),
            "4": (self.task_4, 0, float),
            "5": (self.task_5, 0, float),
            "6.a": (self.task_6_a, 1, str),
            "15": (self.task_15, 1, str),
            "18": (self.task_18, 1, str)
        }

    def execute_task(self, task_number, variables):
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

    def task_1(self, variables):
        x, y = variables if len(variables) == 2 else (1, 2)
        result = (1 + math.sin(x + y) ** 2) / (2 + abs((x - 2 * x) / (1 + x**2 * y**2))) + x
        return "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x", f"x = {x}, y = {y}", result

    def task_2(self, variables):
        x, y = variables if len(variables) == 2 else (1, 2)
        if x <= y:
            x = 0
        result = x, y
        return "x = 0 if x <= y else x, y", f"x = {x}, y = {y}", result

    def task_3_1(self, variables):
        a, n = variables if len(variables) == 2 else (2, 3)
        n = int(n)  # Конвертуємо n в ціле число
        
        # В 1: Через цикл for
        result = 0
        for i in range(1, n + 1):
            result += 1 / (a ** (2 ** i))
        
        return "The sum 1/a + 1/a^2 + ... + 1/a^(2^n)", f"a = {a}, n = {n}", result

    def task_3_2(self, variables):
        a, n = variables if len(variables) == 2 else (2, 3)
        
        # В 2: Через цикл while   
        result = 0
        i = 1
        while i <= n:
            result += 1 / (a ** (2 ** i))
            i += 1

        return "The sum 1/a + 1/a^2 + ... + 1/a^(2^n)", f"a = {a}, n = {n}", result 

    def task_4(self, _):
        return "π^π", "π = 3.141592...", math.pi ** math.pi

    def task_5(self, _):
        return "π * π", "π = 3.141592...", math.pi * math.pi

    def task_6_a(self, variables):
        text = variables[0] if variables else "Hello world! How are you!"
        
        # Знаходимо індекс першого знаку оклику
        exclamation_index = text.find('!')
        if exclamation_index == -1:
            return "No exclamation mark found in the string", f"Input: {text}", 0
        
        # Підраховуємо кількість пробілів до першого знаку оклику
        spaces_count = text[:exclamation_index].count(' ')
        
        return "Count spaces before first exclamation mark", f"Input: {text}", spaces_count

    def task_15(self, variables):
        text = variables[0] if variables else "Hello, world. 3 times, 3 more"
        
        # Знаходимо індекс першої крапки
        dot_index = text.find('.')
        if dot_index == -1:
            return "No dot found in the string", f"Input: {text}", text
            
        # Розділяємо текст на дві частини
        first_part = text[:dot_index].replace(',', '')  # Видаляємо коми в першій частині
        second_part = text[dot_index:].replace('3', '+')  # Замінюємо 3 на + в другій частині
        
        # Об'єднуємо частини
        result = first_part + second_part
        
        return "Remove commas before first dot and replace 3 with + after dot", f"Input: {text}", result

    def text_split(self, text):
        return [word for word in text.split() if word]

    def task_18(self, variables):
        text = variables[0] if variables else "Hello world level deed stats"
        
        # Отримуємо список слів через допоміжну функцію
        words = self.text_split(text)
        
        # Знаходимо слова, де перший і останній символи співпадають
        matching_words = [word for word in words if word and word[0].lower() == word[-1].lower()]
        
        # Формуємо результат
        result = {
            "total_words": len(words),
            "matching_words": matching_words,
            "matching_count": len(matching_words)
        }
        
        return ("Count words where first and last characters match", 
                f"Input: {text}", 
                f"Matching words: {matching_words}\nCount: {len(matching_words)}")
    
    
