# 📋 Технічне завдання CalcMaths

## 📝 Опис задач проєкту

### 📊 Загальна структура задач
Кожна задача в системі має:
- Унікальний ідентифікатор (ID)
- Опис алгоритму
- Специфікацію вхідних даних (типи, обмеження)
- Специфікацію вихідних даних (формат результату)
- Набір прикладів
- Алгоритм розв'язання

### 🧮 Задача 1: Обчислення математичного виразу
**ID:** 1

**Алгоритм:**
1. Прийняти значення змінних x та y
2. Обчислити вираз: (1 + sin²(x + y)) / (2 + abs((x - 2*x) / (1 + x²*y²))) + x
3 Вивести

**Вхідні дані:**
- x: дійсне число
- y: дійсне число

**Вихідні дані:**
- Результат обчислення виразу (дійсне число)

**Приклад:**
- Вхід: x = 2, y = 3
- Вихід: 2.122... (Примітка: фактичний результат обчислення виразу дорівнює приблизно 2.935)

### 🔢 Задача 2: методу Ньютона
**ID:** 2

**Алгоритм:**

Обчислення скінченних різниць для таблиці значень





1. Прийняти значення змінних a та b
2. Якщо a <= b, встановити c = (a + b) / 2
3. Якщо a > b, встановити c = a * b
4. Повернути значення c

**Вхідні дані:**
- a: дійсне число
- b: дійсне число

**Вихідні дані:**
- Значення c (дійсне число)

**Приклади:**
- Вхід: a = 3, b = 5
- Вихід: c = 4.0 (тому що 3 <= 5, отже c = (3 + 5) / 2 = 4.0)

- Вхід: a = 7, b = 2
- Вихід: c = 14.0 (тому що 7 > 2, отже c = 7 * 2 = 14.0)

### 🔢 Задача 2: графічний метод
**ID:** 2

в графік перетворити методу Ньютона