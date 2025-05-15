import numpy as np
import matplotlib.pyplot as plt
from components.math_tasks import calculate_finite_differences

    print("Демонстрація обчислення скінченних різниць")
    print("------------------------------------------")
    
    # Приклад 1: Функція y = x^2
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    
    print("\nПриклад 1: Функція y = x^2")
    print(f"x_values: {x_values}")
    print(f"y_values: {y_values}")
    
    delta_y, delta2_y, delta3_y = calculate_finite_differences(x_values, y_values)
    
    print("\nРезультати обчислення різниць:")
    print(f"Перші різниці: {delta_y}")
    print(f"Другі різниці: {delta2_y}")
    print(f"Треті різниці: {delta3_y}")
    
    # Приклад 2: Функція y = x^3
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 8, 27, 64, 125]
    
    print("\nПриклад 2: Функція y = x^3")
    print(f"x_values: {x_values}")
    print(f"y_values: {y_values}")
    
    delta_y, delta2_y, delta3_y = calculate_finite_differences(x_values, y_values)
    
    print("\nРезультати обчислення різниць:")
    print(f"Перші різниці: {delta_y}")
    print(f"Другі різниці: {delta2_y}")
    print(f"Треті різниці: {delta3_y}")
    

if __name__ == "__main__":
    

