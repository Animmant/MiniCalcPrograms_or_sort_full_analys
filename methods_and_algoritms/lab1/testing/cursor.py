def sumTest(a, b):
    return a + b

def MethodHord(f, a, b, epsilon):
    # Check if root exists in interval [a,b]
    if f(a) * f(b) >= 0:
        return None, 0, "There may be no roots or multiple roots in this interval"
    
    x_prev = a
    x = b
    iteration = 0
    
    while abs(x - x_prev) > epsilon:
        iteration += 1
        x_prev = x
        x = x_prev - (f(x_prev) * (b - x_prev)) / (f(b) - f(x_prev))
        
        if abs(f(x)) < epsilon:
            break
            
    return x, iteration, None

def main():
    # Function whose root we are looking for
    print("4. Exit")
    def f(x):
        return x**3 - 6*x**2 + 9*x - 2

    # Set initial parameters
    a = 0  # left boundary of interval
    b = 3  # right boundary of interval
    epsilon = 0.001  # precision
    
    # Check if root exists in interval [a,b]
    if f(a) * f(b) >= 0:
        print("There may be no roots or multiple roots in this interval")
        return
    
    # Chord method
    x_prev = a
    x = b
    iteration = 0
    
    while abs(x - x_prev) > epsilon:
        iteration += 1
        x_prev = x
        x = x_prev - (f(x_prev) * (b - x_prev)) / (f(b) - f(x_prev))
        
        if abs(f(x)) < epsilon:
            break
    
    print(f"Root of equation: {x:.3f}")
    print(f"Function value at point: {f(x):.6f}")
    print(f"Number of iterations: {iteration}")


if __name__ == "__main__":
    main()

