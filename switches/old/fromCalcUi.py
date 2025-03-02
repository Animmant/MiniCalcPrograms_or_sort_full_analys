import flet as ft
import math

def task_1():
    description = ""
    input_data = "x = 1, y = 2"
    x = 1
    y = 2
    top_formula = 1 + math.sin(x + y) ** 2
    bottom_formula = 2 + abs((x-2*x)/(1+x**2*y**2))
    result = top_formula/bottom_formula + x


    return description, input_data, result

def task_3():
    description = "π * π"
    input_data = "π = 3.141592..."
    result = math.pi * math.pi
    return description, input_data, result

def task_4():
    description = "π^π"
    input_data = "π = 3.141592..."
    result = math.pi ** math.pi
    return description, input_data, result

def task_11():
    description = "the sum 1/a + 1/a^2 + ... + 1/a^(2^n)"
    input_data = "a = 2, n = 3"
    a = 2
    n = 3
    result = sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))
    return description, input_data, result

def execute_task(task_number):
    tasks = {
        "1": task_1,
        "3": task_3,
        "4": task_4,
        "11": task_11,
    }
    if task_number in tasks:
        description, input_data, result = tasks[task_number]()
        return f"{description}\nInput Data: {input_data}\nResult: {result}"
    return "Unknown Task"

def main(page: ft.Page):
    page.title = "Practical Tasks"
    page.scroll = "adaptive"
    
    txt_result = ft.TextField(
        text_align=ft.TextAlign.LEFT, 
        expand=1, 
        read_only=True, 
        multiline=True
    )
    
    def btn_click(e):
        match e.control.text:
            case 'C':
                txt_result.value = ''
            case '=':
                try:
                    txt_result.value = str(eval(txt_result.value))
                except Exception:
                    txt_result.value = 'Error'
            case _:
                txt_result.value = execute_task(e.control.text)
        txt_result.update()
    
    buttons = [str(i) for i in range(1, 16)] + ["2.1", "2.2", "2.3"]
    
    grid = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=80,
        child_aspect_ratio=1,
        spacing=5,
        run_spacing=5,
    )
    
    for btn_text in buttons:
        grid.controls.append(
            ft.TextButton(
                text=btn_text, 
                on_click=btn_click, 
                width=80, 
                height=80
            )
        )
    
    page.add(txt_result, grid)
    page.update()
    
ft.app(target=main)
