import math 

def f(x):
    return x**3 - 6*x**2 + 9*x - 2

def main():
    a = 1.5
    b = 2.5
    epsilon = 0.001

    while True:
        print("Choose an option:")
        print("1. Calculate f(a)")
        print("2. Calculate f(b)")
        print("3. Calculate f(c)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print(f"f({a}) = {f(a)}")
        elif choice == '2':
            print(f"f({b}) = {f(b)}")
        elif choice == '3':
            c = float(input("Enter the value of c: "))
            print(f"f({c}) = {f(c)}")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


