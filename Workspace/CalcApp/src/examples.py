import numpy as np
import matplotlib.pyplot as plt
from src.components.math_task import calculate_finite_differences

def demonstrate_finite_differences():
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
    
    # Приклад 3: Синусоїдальна функція
    x_values = np.linspace(0, 2*np.pi, 10).tolist()
    y_values = np.sin(x_values).tolist()
    
    print("\nПриклад 3: Функція y = sin(x)")
    print(f"x_values: {[round(x, 2) for x in x_values]}")
    print(f"y_values: {[round(y, 4) for y in y_values]}")
    
    delta_y, delta2_y, delta3_y = calculate_finite_differences(x_values, y_values)
    
    print("\nРезультати обчислення різниць:")
    print(f"Перші різниці: {[round(d, 4) for d in delta_y]}")
    print(f"Другі різниці: {[round(d, 4) for d in delta2_y]}")
    print(f"Треті різниці: {[round(d, 4) for d in delta3_y]}")
    
    # Графічна демонстрація
    plot_finite_differences()

def plot_finite_differences():
    """Графічна демонстрація скінченних різниць для функції y = x^2"""
    x_values = np.linspace(0, 5, 6)
    y_values = x_values**2
    
    delta_y, delta2_y, delta3_y = calculate_finite_differences(x_values, y_values)
    
    plt.figure(figsize=(12, 8))
    
    # Графік функції
    plt.subplot(2, 2, 1)
    plt.plot(x_values, y_values, 'o-', linewidth=2, markersize=8)
    plt.title('Функція y = x^2')
    plt.grid(True)
    
    # Графік перших різниць
    plt.subplot(2, 2, 2)
    x_delta = x_values[:-1] + 0.5  # Середини інтервалів
    plt.plot(x_delta, delta_y, 'o-', linewidth=2, markersize=8)
    plt.title('Перші різниці')
    plt.grid(True)
    
    # Графік других різниць
    plt.subplot(2, 2, 3)
    x_delta2 = x_values[:-2] + 1  # Середини інтервалів другого рівня
    plt.plot(x_delta2, delta2_y, 'o-', linewidth=2, markersize=8)
    plt.title('Другі різниці')
    plt.grid(True)
    
    # Графік третіх різниць
    plt.subplot(2, 2, 4)
    x_delta3 = x_values[:-3] + 1.5  # Середини інтервалів третього рівня
    plt.plot(x_delta3, delta3_y, 'o-', linewidth=2, markersize=8)
    plt.title('Треті різниці')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('finite_differences.png')
    print("\nГрафік збережено в файлі 'finite_differences.png'")

if __name__ == "__main__":
    demonstrate_finite_differences()
