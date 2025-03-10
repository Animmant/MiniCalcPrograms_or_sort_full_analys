import flet as ft
from tasks import TaskManager

class UIManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.task_manager = TaskManager()
        self.variable_inputs = []
        self.current_task = None

        # Налаштування сторінки
        self.page.title = "Practical Tasks"
        self.page.scroll = "adaptive"

        # Поля вводу та виводу
        self.txt_input = ft.TextField(
            label="Enter value and press Enter",
            width=200,
            on_submit=self.add_variable
        )

        # Dropdown for examples
        self.examples_dropdown = ft.Dropdown(
            width=300,
            label="Select an example",
            on_change=self.select_example,
            visible=False
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

        # Грід для кнопок задач
        self.grid = ft.GridView(
            expand=1, runs_count=3, max_extent=80, child_aspect_ratio=1, spacing=5, run_spacing=5
        )

        self.create_task_buttons()

        # Кнопка очищення
        self.btn_clear = ft.ElevatedButton(text="Clear", on_click=self.clear_inputs)

        # Додавання компонентів на сторінку
        self.page.add(
            ft.Row([self.txt_input, self.examples_dropdown]),
            self.txt_variables, 
            self.txt_result, 
            self.grid, 
            self.btn_clear
        )
        self.page.update()

    def create_task_buttons(self):
        """Створення кнопок для задач"""
        for task_number in self.task_manager.tasks.keys():
            self.grid.controls.append(
                ft.TextButton(
                    text=task_number,
                    on_click=self.set_task,
                    width=80,
                    height=80,
                    data=False  # Вказує, чи вибрана кнопка
                )
            )

    def set_task(self, e):
        """Вибір задачі та зміна стилю кнопки"""
        # Скидання стилів у всіх кнопок
        for button in self.grid.controls:
            button.style = None
            button.data = False

        # Виділення обраної кнопки
        e.control.style = ft.ButtonStyle(
            bgcolor=ft.colors.GREY_300
        )
        e.control.data = True

        self.current_task = e.control.text
        self.variable_inputs.clear()
        self.txt_variables.value = "Entered values: []"
        self.txt_result.value = "Waiting for inputs..."
        
        # Check if this task has predefined examples
        examples = self.task_manager.get_examples_for_task(self.current_task)
        if examples:
            # Update dropdown with examples
            self.examples_dropdown.options = [
                ft.dropdown.Option(key=key, text=key) for key in examples.keys()
            ]
            self.examples_dropdown.visible = True
        else:
            self.examples_dropdown.options = []
            self.examples_dropdown.visible = False
        
        self.update_ui()

    def select_example(self, e):
        """Handle example selection from dropdown"""
        if not self.examples_dropdown.value or not self.current_task:
            return
            
        examples = self.task_manager.get_examples_for_task(self.current_task)
        if not examples:
            return
            
        selected_example = examples.get(self.examples_dropdown.value)
        if not selected_example:
            return
            
        # For system of linear equations, the example is a string
        if self.current_task == "10":
            self.variable_inputs = [selected_example]
            self.txt_variables.value = f"Selected example: {self.examples_dropdown.value}"
            
            # Execute the task with the selected example
            result = self.task_manager.execute_task(self.current_task, self.variable_inputs)
            self.txt_result.value = result
        
        # For matrix determinant, the example is a numpy array
        elif self.current_task == "det_of_matrix":
            # Convert matrix to string representation for display
            matrix_str = str(selected_example)
            self.variable_inputs = [matrix_str]
            self.txt_variables.value = f"Selected example: {self.examples_dropdown.value}"
            
            # Execute the task with the selected example
            result = self.task_manager.execute_task(self.current_task, self.variable_inputs)
            self.txt_result.value = result
            
        self.update_ui()

    def add_variable(self, e):
        """Додавання змінної після натискання Enter"""
        try:
            value = self.txt_input.value.strip()
            if value:
                self.variable_inputs.append(value)
                self.txt_input.value = ""
                self.txt_variables.value = f"Entered values: {self.variable_inputs}"
            else:
                self.txt_result.value = "Error: Empty input!"
        except ValueError:
            self.txt_result.value = "Error: Invalid input!"

        self.update_ui()

        # Виконання задачі
        if self.current_task:
            result = self.task_manager.execute_task(self.current_task, self.variable_inputs)
            self.txt_result.value = result
            if "Waiting" not in result:
                self.variable_inputs.clear()
        self.update_ui()

    def clear_inputs(self, e):
        """Очищення введених значень"""
        self.variable_inputs.clear()
        self.txt_variables.value = "Entered values: []"
        self.txt_result.value = ""
        self.txt_input.value = ""
        self.examples_dropdown.value = None
        self.update_ui()

    def update_ui(self):
        """Оновлення інтерфейсу"""
        self.txt_result.update()
        self.txt_input.update()
        self.txt_variables.update()
        self.grid.update()
        self.examples_dropdown.update()
