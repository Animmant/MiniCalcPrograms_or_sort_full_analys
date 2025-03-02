import flet as ft
from tasks import TaskManager

class UIManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.task_manager = TaskManager()
        self.variable_inputs = []
        self.current_task = None

        self.page.title = "Practical Tasks"
        self.page.scroll = "adaptive"

        self.txt_input = ft.TextField(
            label="Enter value and press Enter",
            width=200,
            on_submit=self.add_variable
        )

        self.txt_variables = ft.TextField(
            value="Entered values: []",
            read_only=True,
            expand=1,
            multiline=True
        )

        self.txt_result = ft.TextField(
            text_align=ft.TextAlign.LEFT,
            expand=1,
            read_only=True,
            multiline=True
        )

        self.grid = ft.GridView(
            expand=1, runs_count=3, max_extent=80, child_aspect_ratio=1, spacing=5, run_spacing=5
        )

        self.create_task_buttons()

        self.btn_clear = ft.ElevatedButton(text="Clear", on_click=self.clear_inputs)

        self.page.add(self.txt_input, self.txt_variables, self.txt_result, self.grid, self.btn_clear)
        self.page.update()

    def create_task_buttons(self):
        for task_number in self.task_manager.tasks.keys():
            self.grid.controls.append(
                ft.TextButton(
                    text=task_number,
                    on_click=self.set_task,
                    width=80,
                    height=80,
                    data=False
                )
            )

    def set_task(self, e):
        """Вибір задачі"""
        for button in self.grid.controls:
            button.style = None
            button.data = False
            
        e.control.style = ft.ButtonStyle(
            bgcolor=ft.colors.GREY_300
        )
        e.control.data = True
        
        self.current_task = e.control.text
        self.variable_inputs.clear()
        self.txt_variables.value = "Entered values: []"
        self.txt_result.value = "Waiting for inputs..."
        self.update_ui()

    def add_variable(self, e):
        """Додавання змінних після натискання Enter"""
        try:
            value = self.txt_input.value if self.txt_input.value else ""
            self.variable_inputs.append(value)
            self.txt_input.value = ""
            self.txt_variables.value = f"Entered values: {self.variable_inputs}"
        except ValueError:
            self.txt_result.value = "Error: Invalid input!"
        self.update_ui()
        
        if self.current_task:
            self.txt_result.value = self.task_manager.execute_task(self.current_task, self.variable_inputs)
            if "Waiting" not in self.txt_result.value:
                self.variable_inputs.clear()
        self.update_ui()

    def clear_inputs(self, e):
        """Очищення введених значень"""
        self.variable_inputs.clear()
        self.txt_variables.value = "Entered values: []"
        self.txt_result.value = ""
        self.txt_input.value = ""
        self.update_ui()

    def update_ui(self):
        """Оновлення інтерфейсу"""
        self.txt_result.update()
        self.txt_input.update()
        self.txt_variables.update()
        self.grid.update()
