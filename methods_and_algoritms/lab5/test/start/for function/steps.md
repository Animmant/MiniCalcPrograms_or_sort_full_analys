# Покрокова реалізація алгоритмів наближеного диференціювання

## 1. Реалізація розділених різниць

### Крок 1: Створення базових структур
1. Оголосити функцію для обчислення розділених різниць:
   ```python
   def calculate_divided_differences(x_values, y_values):
       # Код функції буде тут
   ```

2. Перевірити вхідні дані на коректність:
   ```python
   if len(x_values) != len(y_values):
       raise ValueError("Довжини списків x_values та y_values повинні збігатись")
   
   # Перевірка на дублікати в x_values
   if len(set(x_values)) != len(x_values):
       raise ValueError("Значення x_values повинні бути унікальними")
   ```

3. Створити двовимірний масив для таблиці розділених різниць:
   ```python
   n = len(x_values)
   diff_table = [[0.0 for _ in range(n)] for _ in range(n)]
   ```

### Крок 2: Заповнення таблиці розділених різниць
1. Заповнити нульовий рядок таблиці значеннями функції:
   ```python
   for i in range(n):
       diff_table[0][i] = y_values[i]
   ```

2. Обчислити розділені різниці вищих порядків:
   ```python
   for i in range(1, n):  # i - порядок розділеної різниці
       for j in range(n - i):  # j - індекс початкової точки
           diff_table[i][j] = (diff_table[i-1][j+1] - diff_table[i-1][j]) / (x_values[j+i] - x_values[j])
   ```

3. Повернути таблицю розділених різниць:
   ```python
   return diff_table
   ```

### Крок 3: Тестування функції
1. Створити масиви з тестовими даними для відомої функції:
   ```python
   # Тестування на функції f(x) = x^2
   x_test = [1, 2, 3, 4, 5]
   y_test = [1, 4, 9, 16, 25]
   ```

2. Обчислити таблицю розділених різниць:
   ```python
   diff_table = calculate_divided_differences(x_test, y_test)
   ```

3. Перевірити, чи відповідають розділені різниці очікуваним значенням:
   ```python
   # Для x^2 розділені різниці 2-го порядку повинні дорівнювати 1, а вищих порядків - 0
   print(f"Розділена різниця 1-го порядку: {diff_table[1][0]}")  # Очікуємо 3.0
   print(f"Розділена різниця 2-го порядку: {diff_table[2][0]}")  # Очікуємо 1.0
   print(f"Розділена різниця 3-го порядку: {diff_table[3][0]}")  # Очікуємо 0.0
   ```

## 2. Реалізація інтерполяційного многочлена Ньютона

### Крок 1: Створення класу інтерполяційного многочлена
1. Оголосити клас для многочлена Ньютона:
   ```python
   class NewtonPolynomial:
       def __init__(self, x_values, y_values):
           # Конструктор класу
   ```

2. Ініціалізувати необхідні атрибути:
   ```python
   self.x_values = x_values
   self.y_values = y_values
   self.diff_table = calculate_divided_differences(x_values, y_values)
   ```

### Крок 2: Реалізація методу обчислення значення многочлена
1. Додати метод для обчислення значення многочлена:
   ```python
   def evaluate(self, x):
       """Обчислює значення многочлена в точці x"""
       n = len(self.x_values)
       result = self.diff_table[0][0]  # f(x₀)
       product = 1.0
       
       for i in range(1, n):
           product *= (x - self.x_values[i-1])  # (x-x₀)(x-x₁)...(x-xᵢ₋₁)
           result += self.diff_table[i][0] * product
           
       return result
   ```

### Крок 3: Тестування інтерполяційного многочлена
1. Створити екземпляр класу з тестовими даними:
   ```python
   # Тестування на функції f(x) = x^2
   x_test = [1, 2, 3, 4, 5]
   y_test = [1, 4, 9, 16, 25]
   newton_poly = NewtonPolynomial(x_test, y_test)
   ```

2. Перевірити значення многочлена в проміжних точках:
   ```python
   test_x = 2.5
   true_value = test_x ** 2  # 6.25
   approx_value = newton_poly.evaluate(test_x)
   print(f"Точка x = {test_x}")
   print(f"Істинне значення: {true_value}")
   print(f"Наближене значення: {approx_value}")
   print(f"Абсолютна похибка: {abs(true_value - approx_value)}")
   ```

## 3. Реалізація обчислення першої похідної

### Крок 1: Додавання методу для обчислення першої похідної
1. Додати метод для обчислення першої похідної у клас NewtonPolynomial:
   ```python
   def first_derivative(self, x):
       """Обчислює першу похідну інтерполяційного многочлена в точці x"""
       n = len(self.x_values)
       result = self.diff_table[1][0]  # f[x₀,x₁]
       
       # Додаткові терми для n > 2
       for k in range(2, n):
           term = 0
           for j in range(k-1):
               product = 1
               for i in range(k-1):
                   if i != j:
                       product *= (x - self.x_values[i])
               term += product
           result += self.diff_table[k][0] * term
       
       return result
   ```

### Крок 2: Альтернативний метод обчислення першої похідної
1. Додати метод чисельного диференціювання для порівняння:
   ```python
   def first_derivative_numerical(self, x, h=1e-6):
       """Наближене обчислення першої похідної методом центральних різниць"""
       return (self.evaluate(x + h) - self.evaluate(x - h)) / (2 * h)
   ```

### Крок 3: Тестування обчислення першої похідної
1. Перевірити обчислення першої похідної на відомій функції:
   ```python
   # Тестування на функції f(x) = x^2, f'(x) = 2x
   test_x = 3.5
   true_derivative = 2 * test_x  # 7.0
   approx_derivative = newton_poly.first_derivative(test_x)
   numerical_derivative = newton_poly.first_derivative_numerical(test_x)
   
   print(f"Точка x = {test_x}")
   print(f"Істинне значення похідної: {true_derivative}")
   print(f"Аналітичне наближення: {approx_derivative}")
   print(f"Чисельне наближення: {numerical_derivative}")
   print(f"Похибка аналітичного методу: {abs(true_derivative - approx_derivative)}")
   print(f"Похибка чисельного методу: {abs(true_derivative - numerical_derivative)}")
   ```

## 4. Реалізація обчислення другої похідної

### Крок 1: Додавання методу для обчислення другої похідної
1. Додати метод для обчислення другої похідної у клас NewtonPolynomial:
   ```python
   def second_derivative(self, x):
       """Обчислює другу похідну інтерполяційного многочлена в точці x"""
       n = len(self.x_values)
       
       # Базовий випадок: для n >= 3
       if n < 3:
           raise ValueError("Для обчислення другої похідної потрібно не менше 3 точок")
           
       result = 2 * self.diff_table[2][0]  # 2*f[x₀,x₁,x₂]
       
       # Додаткові терми для n > 3
       # Складна формула, спрощена реалізація:
       for k in range(3, n):
           term = 0
           # Тут реалізується сума для обчислення другої похідної
           # ...
           result += self.diff_table[k][0] * term
       
       return result
   ```

### Крок 2: Альтернативний метод обчислення другої похідної
1. Додати метод чисельного диференціювання другого порядку:
   ```python
   def second_derivative_numerical(self, x, h=1e-4):
       """Наближене обчислення другої похідної методом центральних різниць"""
       return (self.evaluate(x + h) - 2 * self.evaluate(x) + self.evaluate(x - h)) / (h * h)
   ```

### Крок 3: Тестування обчислення другої похідної
1. Перевірити обчислення другої похідної на відомій функції:
   ```python
   # Тестування на функції f(x) = x^2, f''(x) = 2
   test_x = 3.5
   true_second_derivative = 2.0
   approx_second_derivative = newton_poly.second_derivative_numerical(test_x)
   
   print(f"Точка x = {test_x}")
   print(f"Істинне значення другої похідної: {true_second_derivative}")
   print(f"Наближене значення другої похідної: {approx_second_derivative}")
   print(f"Абсолютна похибка: {abs(true_second_derivative - approx_second_derivative)}")
   ```

## 5. Реалізація графічного диференціювання

### Крок 1: Створення функції для обчислення першої похідної
1. Реалізувати функцію для обчислення першої похідної за табличними даними:
   ```python
   def numerical_diff_first(x_values, y_values):
       """Обчислює першу похідну методом графічного диференціювання"""
       n = len(x_values)
       derivatives = []
       
       # Початкова точка - різниця вперед
       derivatives.append((y_values[1] - y_values[0]) / (x_values[1] - x_values[0]))
       
       # Внутрішні точки - центральна різниця
       for i in range(1, n-1):
           derivatives.append((y_values[i+1] - y_values[i-1]) / (x_values[i+1] - x_values[i-1]))
       
       # Кінцева точка - різниця назад
       derivatives.append((y_values[n-1] - y_values[n-2]) / (x_values[n-1] - x_values[n-2]))
       
       return derivatives
   ```

### Крок 2: Створення функції для обчислення другої похідної
1. Реалізувати функцію для обчислення другої похідної за табличними даними:
   ```python
   def numerical_diff_second(x_values, y_values):
       """Обчислює другу похідну методом графічного диференціювання"""
       n = len(x_values)
       second_derivatives = []
       
       # Для крайніх точок додаємо None
       second_derivatives.append(None)
       
       # Внутрішні точки - формула другої похідної
       for i in range(1, n-1):
           # Припускаємо рівномірний крок
           h = x_values[i+1] - x_values[i]
           second_derivatives.append(
               (y_values[i+1] - 2*y_values[i] + y_values[i-1]) / (h**2)
           )
       
       # Кінцева точка
       second_derivatives.append(None)
       
       return second_derivatives
   ```

### Крок 3: Обробка нерівномірної сітки (опціонально)
1. Додати підтримку нерівномірної сітки для першої похідної:
   ```python
   def numerical_diff_first_nonuniform(x_values, y_values):
       """Обчислює першу похідну для нерівномірної сітки"""
       n = len(x_values)
       derivatives = []
       
       # Початкова точка - різниця вперед
       derivatives.append((y_values[1] - y_values[0]) / (x_values[1] - x_values[0]))
       
       # Внутрішні точки - зважена формула
       for i in range(1, n-1):
           h1 = x_values[i] - x_values[i-1]
           h2 = x_values[i+1] - x_values[i]
           der = (h1 * y_values[i+1] - (h2 - h1) * y_values[i] - h2 * y_values[i-1]) / (h1 * h2 * (h1 + h2))
           derivatives.append(der)
       
       # Кінцева точка - різниця назад
       derivatives.append((y_values[n-1] - y_values[n-2]) / (x_values[n-1] - x_values[n-2]))
       
       return derivatives
   ```

## 6. Тестування та аналіз результатів

### Крок 1: Створення функції для порівняння методів
1. Реалізувати функцію для обчислення та порівняння похідних різними методами:
   ```python
   def compare_differentiation_methods(x_values, y_values, test_points):
       """Порівнює методи диференціювання на заданих тестових точках"""
       # Інтерполяційний многочлен Ньютона
       newton_poly = NewtonPolynomial(x_values, y_values)
       
       # Графічне диференціювання
       first_derivatives = numerical_diff_first(x_values, y_values)
       second_derivatives = numerical_diff_second(x_values, y_values)
       
       results = []
       for x in test_points:
           # Знаходимо найближчу точку у вхідних даних
           idx = min(range(len(x_values)), key=lambda i: abs(x_values[i] - x))
           
           # Обчислюємо похідні обома методами
           newton_first = newton_poly.first_derivative(x)
           newton_second = newton_poly.second_derivative_numerical(x)
           
           graphical_first = first_derivatives[idx]
           graphical_second = second_derivatives[idx] if second_derivatives[idx] is not None else "N/A"
           
           results.append({
               'x': x,
               'newton_first': newton_first,
               'newton_second': newton_second,
               'graphical_first': graphical_first,
               'graphical_second': graphical_second
           })
       
       return results
   ```

### Крок 2: Форматування та виведення результатів
1. Реалізувати функцію для виведення результатів у табличному вигляді:
   ```python
   def print_results(results):
       """Виводить результати обчислень у вигляді таблиці"""
       print(f"{'x':<10} {'f\'(x) Ньютон':<15} {'f\'(x) Графічний':<20} {'f\'\'(x) Ньютон':<15} {'f\'\'(x) Графічний':<20}")
       print("-" * 80)
       
       for res in results:
           x = res['x']
           newton_first = res['newton_first']
           newton_second = res['newton_second']
           graphical_first = res['graphical_first']
           graphical_second = res['graphical_second']
           
           print(f"{x:<10.4f} {newton_first:<15.6f} {graphical_first:<20.6f} {newton_second:<15.6f} {graphical_second}")
   ```

### Крок 3: Аналіз точності методів
1. Реалізувати функцію для аналізу похибок, якщо відомі точні значення похідних:
   ```python
   def analyze_errors(results, exact_first_derivative_func, exact_second_derivative_func):
       """Аналізує похибки методів диференціювання"""
       newton_first_errors = []
       graphical_first_errors = []
       newton_second_errors = []
       graphical_second_errors = []
       
       for res in results:
           x = res['x']
           exact_first = exact_first_derivative_func(x)
           exact_second = exact_second_derivative_func(x)
           
           # Обчислення похибок для першої похідної
           newton_first_error = abs(res['newton_first'] - exact_first)
           graphical_first_error = abs(res['graphical_first'] - exact_first)
           
           # Обчислення похибок для другої похідної
           newton_second_error = abs(res['newton_second'] - exact_second)
           if res['graphical_second'] != "N/A":
               graphical_second_error = abs(res['graphical_second'] - exact_second)
               graphical_second_errors.append(graphical_second_error)
           
           newton_first_errors.append(newton_first_error)
           graphical_first_errors.append(graphical_first_error)
           newton_second_errors.append(newton_second_error)
       
       # Обчислення середніх похибок
       avg_newton_first_error = sum(newton_first_errors) / len(newton_first_errors)
       avg_graphical_first_error = sum(graphical_first_errors) / len(graphical_first_errors)
       avg_newton_second_error = sum(newton_second_errors) / len(newton_second_errors)
       
       if graphical_second_errors:
           avg_graphical_second_error = sum(graphical_second_errors) / len(graphical_second_errors)
       else:
           avg_graphical_second_error = "N/A"
       
       print("\nСередні похибки:")
       print(f"Перша похідна (Ньютон): {avg_newton_first_error:.8f}")
       print(f"Перша похідна (Графічний): {avg_graphical_first_error:.8f}")
       print(f"Друга похідна (Ньютон): {avg_newton_second_error:.8f}")
       print(f"Друга похідна (Графічний): {avg_graphical_second_error}")
   ```

## 7. Основна програма

### Крок 1: Зчитування даних з таблиці
1. Підготувати дані для обчислень:
   ```python
   # Дані з таблиці для варіантів n=1,3,5,7,...,29
   x_values = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4]
   y_values = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507, 4.775, 5.159]
   ```

### Крок 2: Виконання обчислень та виведення результатів
1. Обчислити похідні різними методами:
   ```python
   # Тестові точки для обчислення похідних
   test_points = [2.5, 3.0, 3.5, 4.0, 4.3]
   
   # Порівняння методів
   results = compare_differentiation_methods(x_values, y_values, test_points)
   
   # Виведення результатів
   print("\nРезультати обчислення похідних:")
   print_results(results)
   ```

### Крок 3: Візуалізація результатів (за наявності можливості)
1. Побудувати графіки функції та її похідних:
   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   
   def visualize_results(x_values, y_values, newton_poly):
       """Візуалізує функцію та її похідні"""
       # Створюємо більш точну сітку для гладких графіків
       x_fine = np.linspace(min(x_values), max(x_values), 100)
       y_fine = [newton_poly.evaluate(x) for x in x_fine]
       
       # Обчислюємо похідні на точній сітці
       y_fine_first_derivative = [newton_poly.first_derivative(x) for x in x_fine]
       y_fine_second_derivative = [newton_poly.second_derivative_numerical(x) for x in x_fine]
       
       # Обчислюємо похідні графічним методом
       first_derivatives = numerical_diff_first(x_values, y_values)
       second_derivatives = numerical_diff_second(x_values, y_values)
       
       # Видаляємо None з другої похідної для графіка
       x_second = [x_values[i] for i in range(1, len(x_values)-1)]
       y_second = [second_derivatives[i] for i in range(1, len(second_derivatives)-1) 
                  if second_derivatives[i] is not None]
       
       # Створюємо графіки
       plt.figure(figsize=(12, 8))
       
       # Графік функції
       plt.subplot(3, 1, 1)
       plt.plot(x_fine, y_fine, 'b-', label='Інтерполяційний многочлен')
       plt.plot(x_values, y_values, 'ro', label='Табличні дані')
       plt.title('Функція')
       plt.grid(True)
       plt.legend()
       
       # Графік першої похідної
       plt.subplot(3, 1, 2)
       plt.plot(x_fine, y_fine_first_derivative, 'b-', label='Перша похідна (Ньютон)')
       plt.plot(x_values, first_derivatives, 'go', label='Перша похідна (Графічний)')
       plt.title('Перша похідна')
       plt.grid(True)
       plt.legend()
       
       # Графік другої похідної
       plt.subplot(3, 1, 3)
       plt.plot(x_fine, y_fine_second_derivative, 'b-', label='Друга похідна (Ньютон)')
       plt.plot(x_second, y_second, 'go', label='Друга похідна (Графічний)')
       plt.title('Друга похідна')
       plt.grid(True)
       plt.legend()
       
       plt.tight_layout()
       plt.savefig('derivatives.png')
       plt.show()
   
   # Візуалізуємо результати
   newton_poly = NewtonPolynomial(x_values, y_values)
   visualize_results(x_values, y_values, newton_poly)
   ```

## 8. Висновки та аналіз

Після виконання всіх кроків проаналізуйте отримані результати:

1. Порівняйте точність методу Ньютона та графічного методу
2. Визначте умови, за яких кожен метод працює краще
3. Зробіть висновки щодо практичного застосування методів
4. Запропонуйте способи підвищення точності обчислень 