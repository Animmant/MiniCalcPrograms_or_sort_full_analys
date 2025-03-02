import math

def f(x):
    return x + math.cos(x) - 1


def chord_method(f, a, b, tol=1e-3, max_iter=100):
    for _ in range(max_iter):
        x_new = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(x_new)) < tol:
            print(x_new, max_iter)
            return x_new
        a, b = b, x_new
    return None  # Якщо не збігся

print(chord_method(f, -0.5, 0.5))