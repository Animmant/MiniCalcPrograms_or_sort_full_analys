import math
import utils.hello as hello
from components.math_tasks import plot_newton_interpolation, approximate_derivative_newton

def main(): 
    points_example = [
        (0, math.sin(0)),
        (math.pi/2, math.sin(math.pi/2)),
        (math.pi, math.sin(math.pi)),
        (3*math.pi/2, math.sin(3*math.pi/2)),
        (2*math.pi, math.sin(2*math.pi))
    ]
    # Очікувана похідна sin(x) в x=pi/4: f'(x)=cos(x), f'(pi/4) = cos(pi/4) ≈ 0.707
    x0_eval_example = math.pi / 4

    print(f"Приклад точок для інтерполяції: {points_example}")
    print(f"Точка для обчислення похідної: x0 = {x0_eval_example}")

    try:
        # Обчислюємо наближену похідну в точці x0_eval_example
        approx_deriv = approximate_derivative_newton(points_example, x0_eval_example)
        print(f"Наближене значення похідної в точці {x0_eval_example}: {approx_deriv}")

        # Будуємо графік полінома та похідної
        plot_newton_interpolation(points_example)

    except ValueError as e:
        print(f"Помилка при виконанні: {e}")
    except Exception as e:
        print(f"Неочікувана помилка: {e}")

if __name__ == "__main__":
    main()



