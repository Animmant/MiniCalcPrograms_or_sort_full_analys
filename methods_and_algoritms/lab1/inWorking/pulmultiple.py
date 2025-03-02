import flet as ft
import math

def cosmic_formula(x, y):
    return (1 + math.sin(x + y) ** 2) / (2 + abs((x - 2 * x) / (1 + x**2 * y**2))) + x

def task_1(variables):
    x, y = variables
    return "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x", f"x = {x}, y = {y}", cosmic_formula(x, y)

def task_3(_):
    return "π * π", "π = 3.141592...", math.pi * math.pi

def task_4(_):
    return "π^π", "π = 3.141592...", math.pi ** math.pi

def task_11(variables):
    a, n = variables
    return "the sum 1/a + 1/a^2 + ... + 1/a^(2^n)", f"a = {a}, n = {n}", sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))

def execute_task(task_number, variables):
    tasks = {"1": task_1, "3": task_3, "4": task_4, "11": task_11}
    if task_number in tasks:
        description, input_data, result = tasks[task_number](variables)
        return f"{description}\nInput Data: {input_data}\nResult: {result}"
    return "Unknown Task"

def main(page: ft.Page):
    page.title = "Practical Tasks"
    page.scroll = "adaptive"
    
    variable_inputs = []  # Список для введених значень
    txt_input = ft.TextField(label="Enter value and press Enter", width=200, on_submit=lambda e: add_variable(e))
    txt_result = ft.TextField(text_align=ft.TextAlign.LEFT, expand=1, read_only=True, multiline=True)
    
    def add_variable(e):
        """Додає введене значення до списку"""
        try:
            variable_inputs.append(float(txt_input.value))
            txt_input.value = ""  # Очищення поля після введення
        except ValueError:
            txt_result.value = "Error: Invalid input!"
        txt_result.update()
        txt_input.update()
    
    def calculate(e):
        """Обчислює значення задачі"""
        task_number = e.control.text
        txt_result.value = execute_task(task_number, variable_inputs)
        variable_inputs.clear()  # Очищення списку після обчислення
        txt_result.update()
    
    buttons = [str(i) for i in range(1, 16)] + ["2.1", "2.2", "2.3"]
    grid = ft.GridView(expand=1, runs_count=3, max_extent=80, child_aspect_ratio=1, spacing=5, run_spacing=5)
    
    for btn_text in buttons:
        grid.controls.append(ft.TextButton(text=btn_text, on_click=calculate, width=80, height=80))
    
    page.add(txt_input, txt_result, grid)
    page.update()
    
ft.app(target=main)