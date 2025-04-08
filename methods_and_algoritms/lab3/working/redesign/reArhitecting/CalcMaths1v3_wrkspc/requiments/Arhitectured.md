# 🏗️ Архітектура проєкту CalcMaths

## Загальна структура

```plantuml
@startuml
package "CalcMaths" {
  [main.py] --> [ui.py]
  [ui.py] --> [tasks]
}
@enduml 

### Потік даних

Користувач вибирає задачу з сітки кнопок
Користувач вводить необхідні дані
UI відправляє дані до TaskManager
TaskManager обробляє задачу і повертає результат
UI відображає результат користувачу

### Структура директорій

CopyCalcMaths1v3_wrkspc/
├── main.py                  # Точка входу
├── ui.py                    # Управління інтерфейсом
├── tasks/
│   ├── __init__.py           # Ініціалізує  задач
│   ├── task_manager.py       # Переміщений TaskManager
│   ├── math_tasks.py         # Математичні задачі
│   ├── text_tasks.py         # Текстові задачі
├── README.md                # Загальний опис проєкту
└── requiments/              # Документація
    ├── Architecture.md      # Детальний опис архітектури
    ├── Ideas.md             # Ідеї для розвитку
    ├── Task.md              # Опис завдання
    ├── TaskTemplate.md      # Шаблон для нових задач
    └── Development.md       # Настанови для розробників
└── tests/
    ├── __init__.py
    ├── test_math_tasks.py
    └── test_text_tasks.py