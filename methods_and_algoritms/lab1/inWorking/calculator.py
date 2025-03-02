import flet as ft
import math

def main(page: ft.Page):
    page.title = "Практичні завдання"
    page.scroll = "adaptive"  # Прокрутка для великої кількості кнопок
    
    txt_result = ft.TextField(text_align=ft.TextAlign.RIGHT, expand=1, read_only=True)
    
    def btn_click(e):
        match e.control.text:
            case 'C':
                txt_result.value = ''
            case '=':
                try:
                    txt_result.value = str(eval(txt_result.value))
                except Exception:
                    txt_result.value = 'Error'
            case '3':  # π * π
                txt_result.value = str(math.pi * math.pi)
            case '4':  # π^π
                txt_result.value = str(math.pi ** math.pi)
            case '11':  # Обчислення формули з картинки
                a = 2  # Можна змінювати вхідні дані
                n = 3  # Кількість ітерацій
                result = sum(1 / (a ** (2 ** i)) for i in range(1, n + 1))
                txt_result.value = str(result)
            case _:
                txt_result.value += e.control.text

        txt_result.update()
    
    # Генеруємо номери кнопок від 1 до 15
    buttons = [str(i) for i in range(1, 16)]
    
    grid = ft.GridView(
        expand=1,
        runs_count=3,  # 3 стовпці
        max_extent=80,  # Розмір кнопок
        child_aspect_ratio=1,  # Квадратні кнопки
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
