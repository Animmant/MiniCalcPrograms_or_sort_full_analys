




## Структура проекту

src/
├── main.py                  # Точка входу
├── ui.py                    # Управління інтерфейсом
├── tasks/
│   ├── __init__.py
│   ├── math_tasks.py         # Математичні задачі
│   ├── text_tasks.py         # Текстові задачі
├── README.md                # Загальний опис проєкту
├── utils/                # Допоміжні утиліти
│   ├── validator.py      # Валідація вхідних даних
│   └── error_handlers.py # Обробка помилок
└── tests/
    ├── test_math_tasks.py
    └── test_text_tasks.py
