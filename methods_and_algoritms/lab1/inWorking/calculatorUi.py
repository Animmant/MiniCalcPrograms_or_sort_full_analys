import flet as ft

def main(page: ft.Page):
    page.title = "Calculator App"
    page.scroll = "adaptive"
    page.update()

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
            case _:
                txt_result.value += e.control.text

        txt_result.update()

    buttons = ["789", "456", "123", "0.C", "=-"]

    for row in buttons:
        row_controls = []
        for btn_text in row:
            btn = ft.TextButton(text=btn_text, on_click=btn_click, expand=1)
            row_controls.append(btn)
        page.add(ft.Row(controls=row_controls, expand=1))

    page.add(txt_result)

ft.app(target=main)
