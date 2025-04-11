import math

def calculate_finite_differences(x_values, y_values):
    """
    Обчислює скінченні різниці для інтерполяційного многочлена Ньютона.
    """
    n = len(y_values)
    h = x_values[1] - x_values[0]  # Крок (за умови рівномірної сітки)
    
    # Обчислення скінченних різниць
    delta_y = [y_values[i+1] - y_values[i] for i in range(n-1)]
    delta2_y = [delta_y[i+1] - delta_y[i] for i in range(len(delta_y)-1)]
    delta3_y = [delta2_y[i+1] - delta2_y[i] for i in range(len(delta2_y)-1)]
    
    return delta_y, delta2_y, delta3_y