import flet as ft
import math

def cosmic_formula(x=1, y=2):
    top_formula = 1 + math.sin(x + y) ** 2
    bottom_formula = 2 + abs((x - 2 * x) / (1 + x**2 * y**2))
    return top_formula / bottom_formula + x

def task_1(variables):
    x, y = variables if len(variables) == 2 else (1, 2)  # Дефолтні значення
    return "1 + sin(x + y) ** 2 / (2 + abs((x - 2*x)/(1+x**2*y**2))) + x", f"x = {x}, y = {y}", cosmic_formula(x, y)

def task_3(_):
    return "π * π", "π = 3.141592...", math.pi * math.pi

def task_4(_):
    return "π^π", "π = 3.141592...", math.pi ** math.pi

def task_11(variables):
    a, n = variables if len(variables) == 2 else (2, 3)  # Дефолтні значення
    return "the sum 1/a + 1/a^2 + ... + 1/a^(2^n)", f"a = {a}, n = {n}", sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))

def execute_task(task_number, variables):
    tasks = {"1": (task_1, 2), "3": (task_3, 0), "4": (task_4, 0), "11": (task_11, 2)}
    
    if task_number in tasks:
        task_function, required_vars = tasks[task_number]
        if len(variables) >= required_vars:
            description, input_data, result = task_function(variables)
            return f"{description}\nInput Data: {input_data}\nResult: {result}"
        return f"Waiting for {required_vars - len(variables)} more input(s)..."
    return "Unknown Task"

def add_variable(e, txt_input, txt_variables, txt_result, variable_inputs, current_task):
    try:
        variable_inputs.append(float(txt_input.value) if txt_input.value else 1)  # Дефолтне значення = 1
        txt_input.value = ""
        txt_variables.value = f"Entered values: {variable_inputs}"
    except ValueError:
        txt_result.value = "Error: Invalid input!"
    txt_result.update()
    txt_input.update()
    txt_variables.update()

    # Перевіряємо, чи вистачає змінних для виконання задачі
    tasks = {"1": 2, "11": 2}  # Очікувана кількість змінних для задач
    if current_task in tasks and len(variable_inputs) >= tasks[current_task]:
        txt_result.value = execute_task(current_task, variable_inputs)
        variable_inputs.clear()  # Очищуємо список після виконання
    txt_result.update()


def set_task(e, txt_variables, txt_result, variable_inputs, current_task):
    current_task = e.control.text
    variable_inputs.clear()
    txt_variables.value = "Entered values: []"
    txt_result.value = "Waiting for inputs..."
    txt_result.update()
    txt_variables.update()
    return current_task

def clear_inputs(e, txt_variables, txt_result, txt_input, variable_inputs):
    variable_inputs.clear()
    txt_variables.value = "Entered values: []"
    txt_result.value = ""
    txt_input.value = ""
    txt_variables.update()
    txt_result.update()
    txt_input.update()

def main(page: ft.Page):
    page.title = "Practical Tasks"
    page.scroll = "adaptive"
    
    variable_inputs = []
    current_task = None
    
    txt_input = ft.TextField(label="Enter value and press Enter", width=200, on_submit=lambda e: add_variable(e, txt_input, txt_variables, txt_result, variable_inputs, current_task))
    txt_variables = ft.TextField(value="Entered values: []", read_only=True, expand=1, multiline=True)
    txt_result = ft.TextField(text_align=ft.TextAlign.LEFT, expand=1, read_only=True, multiline=True)
    
    buttons = ["1", "3", "4", "11"]
    grid = ft.GridView(expand=1, runs_count=3, max_extent=80, child_aspect_ratio=1, spacing=5, run_spacing=5)
    
    for btn_text in buttons:
        grid.controls.append(ft.TextButton(text=btn_text, on_click=lambda e: set_task(e, txt_variables, txt_result, variable_inputs, current_task), width=80, height=80))
    
    btn_clear = ft.ElevatedButton(text="Clear", on_click=lambda e: clear_inputs(e, txt_variables, txt_result, txt_input, variable_inputs))
    
    page.add(txt_input, txt_variables, txt_result, grid, btn_clear)
    page.update()
    
ft.app(target=main)
