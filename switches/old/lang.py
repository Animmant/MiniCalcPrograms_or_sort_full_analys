import flet as ft
import math

# Translation dictionary for multiple languages
translations = {
    'ua': {
        'task_3_desc': "Обчислити π * π",
        'task_3_input': "π = 3.141592...",
        'task_4_desc': "Обчислити π^π",
        'task_4_input': "π = 3.141592...",
        'task_11_desc': "Обчислити суму 1/a + 1/a^2 + ... + 1/a^(2^n)",
        'task_11_input': "a = 2, n = 3",
        'unknown_task': "Невідома задача",
        'page_title': "Практичні завдання",
        'error': "Помилка"
    },
    'en': {
        'task_3_desc': "Calculate π * π",
        'task_3_input': "π = 3.141592...",
        'task_4_desc': "Calculate π^π",
        'task_4_input': "π = 3.141592...",
        'task_11_desc': "Calculate the sum 1/a + 1/a^2 + ... + 1/a^(2^n)",
        'task_11_input': "a = 2, n = 3",
        'unknown_task': "Unknown Task",
        'page_title': "Practical Tasks",
        'error': "Error"
    }
}

# Set the current language. Change this value to "ua" or "en" as needed.
current_lang = 'en'

def task_3():
    description = translations[current_lang]['task_3_desc']
    input_data = translations[current_lang]['task_3_input']
    result = math.pi * math.pi
    return description, input_data, result

def task_4():
    description = translations[current_lang]['task_4_desc']
    input_data = translations[current_lang]['task_4_input']
    result = math.pi ** math.pi
    return description, input_data, result

def task_11():
    description = translations[current_lang]['task_11_desc']
    input_data = translations[current_lang]['task_11_input']
    a = 2
    n = 3
    result = sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))
    return description, input_data, result

def execute_task(task_number):
    tasks = {
        "3": task_3,
        "4": task_4,
        "11": task_11,
    }
    if task_number in tasks:
        description, input_data, result = tasks[task_number]()
        # Note: The label "Вхідні дані:" is hardcoded below;
        # you might also want to add it into the translations dictionary if desired.
        return f"{description}\nВхідні дані: {input_data}\nРезультат: {result}"
    return translations[current_lang]['unknown_task']

def main(page: ft.Page):
    page.title = translations[current_lang]['page_title']
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
                    txt_result.value = translations[current_lang]['error']
            case _:
                txt_result.value = execute_task(e.control.text)
        txt_result.update()

    buttons = [str(i) for i in range(1, 16)]

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