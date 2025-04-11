from components.math_task import calculate_expression

def main():
    print("Калькулятор математичного виразу")
    print("(1 + sin²(x + y)) / (2 + abs((x - 2*x) / (1 + x²*y²))) + x")
    
    try:
        x = float(input("Введіть значення x: "))
        y = float(input("Введіть значення y: "))
        
        result = calculate_expression(x, y)
        
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")

if __name__ == "__main__":
    main()
