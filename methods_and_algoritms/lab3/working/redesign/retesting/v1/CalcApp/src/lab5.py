import components.math_task as math_task
import numpy as np

def parse_float_list(input_str: str) -> list[float]:
    """Парсить рядок чисел, розділених комами або пробілами, у список float."""
    parts = input_str.replace(',', ' ').split()
    return [float(part) for part in parts]

def main():
    print("Обчислення першої та другої похідної методом Ньютона")
    print("---------------------------------------------------")
    
    try:
        # Введення даних
        x_str = input("Введіть значення x (числа через пробіл або кому): ")
        y_str = input("Введіть відповідні значення y (числа через пробіл іабо кому): ")
        at_point_str = input("Введіть точку, в якій обчислити похідні: ")
        
        # Парсинг введених даних
        x_values = parse_float_list(x_str)
        y_values = parse_float_list(y_str)
        at_point = float(at_point_str)
        
        # Перевірка відповідності кількості x та y
        if len(x_values) != len(y_values):
            print("Помилка: Кількість значень x та y має бути однаковою.")
            return
            
        if len(x_values) < 2:
             print("Помилка: Для обчислення похідних потрібно щонайменше дві точки.")
             return

        # Обчислення похідних
        first_derivative, second_derivative = math_task.newton_derivatives(x_values, y_values, at_point)
        
        # Виведення результату
        print("\nРезультат:")
        print(f"Перша похідна в точці {at_point}: {first_derivative:.6f}")
        print(f"Друга похідна в точці {at_point}: {second_derivative:.6f}")
        
    except ValueError:
        print("Помилка: Некоректний формат введених даних. Будь ласка, введіть числа.")
    except IndexError:
         print("Помилка: Недостатньо даних для обчислення похідних (можливо, помилка в функції newton_derivatives або даних).") # На випадок, якщо dd[1] не існує
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")

if __name__ == "__main__":
    main()
