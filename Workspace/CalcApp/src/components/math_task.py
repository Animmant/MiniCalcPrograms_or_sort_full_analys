import math

def calculate_expression(x: float, y: float) -> float:
   
    # Обчислюємо sin²(x + y)
    sin_squared = math.pow(math.sin(x + y), 2)
    
    # Обчислюємо x²*y²
    x_squared_y_squared = math.pow(x, 2) * math.pow(y, 2)
    
    # Обчислюємо (x - 2*x), це дорівнює -x
    x_minus_2x = x - 2 * x
    
    # Обчислюємо знаменник дробу (x - 2*x) / (1 + x²*y²)
    denominator = 1 + x_squared_y_squared
    
    # Перевіряємо, чи знаменник не дорівнює нулю
    if denominator == 0:
        raise ValueError("Знаменник виразу дорівнює нулю, ділення неможливе")
    
    # Обчислюємо дріб (x - 2*x) / (1 + x²*y²)
    fraction = x_minus_2x / denominator
    
    # Обчислюємо абсолютне значення дробу
    abs_fraction = abs(fraction)
    
    # Обчислюємо знаменник основного виразу
    main_denominator = 2 + abs_fraction
    
    # Перевіряємо, чи знаменник основного виразу не дорівнює нулю
    if main_denominator == 0:
        raise ValueError("Знаменник основного виразу дорівнює нулю, ділення неможливе")
    
    # Обчислюємо основний дріб
    main_fraction = (1 + sin_squared) / main_denominator
    
    # Повертаємо кінцевий результат
    return main_fraction + x

def calculate_differences(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    return table[0]

def newton_derivatives(x: list[float], y: list[float], at_point: float):
    dd = calculate_differences(x, y)
    n = len(x)
    f1 = dd[1]
    f2 = 0.0

    # Перша та друга похідні через формулу Тейлора
    for i in range(2, n):
        term = dd[i]
        for j in range(i - 1):
            term *= (at_point - x[j])
        f1 += term * i / (at_point - x[0])
    
    for i in range(2, n):
        term = dd[i]
        for j in range(i - 2):
            term *= (at_point - x[j])
        f2 += term * i * (i - 1) / ((at_point - x[0]) ** 2)

    return f1, f2


