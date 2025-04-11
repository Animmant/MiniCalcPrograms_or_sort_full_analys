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
