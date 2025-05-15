import math
import numpy

def calculate_expression(x: float, y: float) -> float:
    """Використовує змінні для позначення логічних частин формули."""
    numerator_part1 = 1 + math.pow(math.sin(x + y), 2)
    
    inner_fraction_numerator = -x # x - 2*x
    inner_fraction_denominator = 1 + math.pow(x, 2) * math.pow(y, 2)
    
    if inner_fraction_denominator == 0:
        raise ValueError("Знаменник внутрішнього дробу дорівнює нулю.")
        
    inner_fraction_abs = abs(inner_fraction_numerator / inner_fraction_denominator)
    
    denominator_part2 = 2 + inner_fraction_abs
    
    if denominator_part2 == 0:
        raise ValueError("Знаменник основного виразу дорівнює нулю.")
        
    return numerator_part1 / denominator_part2 + x

def calculate_differences(x, y):
    n = len(x)
    table = numpy.zeros((n, n))
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


