import flet as ft
import math

def cosmic_formula(x, y):
    top_formula = 1 + math.sin(x + y) ** 2
    bottom_formula = 2 + abs((x - 2 * x) / (1 + x**2 * y**2))
    return top_formula / bottom_formula + x

def task_1(x, y):
    description = "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x"
    input_data = f"x = {x}, y = {y}"
    result = cosmic_formula(x, y)
    return description, input_data, str(result)

def task_3():
    description = "π * π"
    input_data = "π = 3.141592..."
    result = math.pi * math.pi
    return description, input_data, str(result)

def task_4():
    description = "π^π"
    input_data = "π = 3.141592..."
    result = math.pi ** math.pi
    return description, input_data, str(result)

def task_11():
    description = "the sum 1/a + 1/a^2 + ... + 1/a^(2^n)"
    input_data = "a = 2, n = 3"
    a = 2
    n = 3
    result = sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))
    return description, input_data, str(result)

def execute_task(task_number):
    tasks = {
        "3": task_3,
        "4": task_4,
        "11": task_11,
    }
    if task_number in tasks:
        description, input_data, result = tasks[task_number]()
        return f"{description}\nInput Data: {input_data}\nResult: {result}"
    return "Unknown Task"

def main(page: ft.Page):
    page.title = "Dynamic Named Variables"

    variables = {}  # Зберігатиме змінні
    input_fields = ft.Column()

    txt_result = ft.TextField(text_align=ft.TextAlign.LEFT, expand=1, read_only=True, multiline=True)

    def add_variable(e):
        """Додає нове поле з іменем"""
        var_name = f"Var {len(variables) + 1}"
        txt_field = ft.TextField(label=var_name)
        variables[var_name] = txt_field
        input_fields.controls.append(txt_field)
        page.update()

    def calculate(e):
        """Обчислення значень усіх змінних"""
        try:
            values = {name: float(field.value) for name, field in variables.items() if field.value}
            txt_result.value = f"Values: {values}\nSum: {sum(values.values())}"
        except ValueError:
            txt_result.value = "Error: Invalid input!"
        txt_result.update()

    # Кнопки
    btn_add = ft.ElevatedButton(text="Add Variable", on_click=add_variable)
    btn_calc = ft.ElevatedButton(text="Calculate", on_click=calculate)

    page.add(btn_add, input_fields, btn_calc, txt_result)
    page.update()

ft.app(target=main)
