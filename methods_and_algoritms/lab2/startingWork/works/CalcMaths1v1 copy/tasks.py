from scipy.optimize import root_scalar, fixed_point
import math

class TaskManager:
    def __init__(self):
        self.tasks = {
            "methods": (self.task_find_root_methods, 0, float),
            "hord": (self.task_find_root_hord, 0, float)
        }
    
    def execute_task(self, task_number, variables):
        if task_number not in self.tasks:
            return "Unknown Task"
        
        task_function, required_vars, data_type = self.tasks[task_number]
        if len(variables) < required_vars:
            remaining = required_vars - len(variables)
            return f"Waiting for {remaining} more input(s)... (Enter {remaining} value{'s' if remaining > 1 else ''})"
        
        try:
            converted_variables = [data_type(var) for var in variables]
            description, input_data, result = task_function(converted_variables)
            return f"{description}\nInput Data: {input_data}\nResult: {result}"
        except Exception as e:
            return f"Error during calculation: {str(e)}"
        
    def init_eq(self, x):
        return x + math.cos(x) - 1

    def task_find_root_methods(self, variables):
        a, b = (-0.5, 0.5) if len(variables) < 2 else (float(variables[0]), float(variables[1]))

        print(f"Using interval: [{a}, {b}]")
        accuracy = 1e-2  # Точність знаходження кореня
        
        # Перевіряємо чи є корінь у заданому інтервалі
        if self.init_eq(a) * self.init_eq(b) >= 0:
            return "Root finding methods", f"Interval: [{a}, {b}]", "No root found in the interval"

        methods = {
            "Chord": {"method": "secant", "x0": a, "x1": b, "xtol": accuracy},
            "Newton": {"method": "newton", "x0": b, "fprime": lambda x: 1 - math.sin(x), "xtol": accuracy},
            "Brentq": {"method": "brentq", "bracket": (a, b), "xtol": accuracy}, 
            "Bisection": {"method": "bisect", "bracket": (a, b), "xtol": accuracy},  
        }

        results = {}

        for name, params in methods.items():
            try:
                result = root_scalar(self.init_eq, **params, maxiter=100)
                if not result.converged:
                    results[name] = "Did not converge within 100 iterations"
                else:
                    results[name] = f"Root: {result.root:.12f}, Iterations: {result.iterations}, Precision: {accuracy}"
            except ValueError as e:
                results[name] = f"Error: {str(e)}"
            except Exception as e:
                results[name] = f"Unexpected Error: {str(e)}"

        # Метод фіксованої точки (окремо від root_scalar)
        try:
            fixed_point_root = fixed_point(lambda x: 1 - math.cos(x), b, xtol=accuracy)
            results["Fixed-Point Iteration"] = f"Root: {fixed_point_root:.6f}, Precision: {accuracy}"
        except Exception as e:
            results["Fixed-Point Iteration"] = f"Error: {str(e)}"

        return "Root finding methods", f"Interval: [{a}, {b}]", results
    
    def task_find_root_hord(self, variables):
        if len(variables) < 2:
            a, b = -0.5, 0.5
        else:
            a, b = float(variables[0]), float(variables[1])
        
        print(f"Using interval: [{a}, {b}]")


        result = self.find_root_hord(self.init_eq, a, b, 1e-3, 1000)
        
        return (
            "Finding root using Chord method", 
            f"Interval: [{a}, {b}]",
            result
        )
    
    def find_root_hord(self, f, a, b, accuracy=1e-3, max_iterations=1000):
        
        if f(a) * f(b) >= 0:
            return "No root in the given interval or method unsuitable"

        for i in range(max_iterations):
            # Обчислюємо нове наближення
            try:
                x_new = b - (f(b) * (b - a)) / (f(b) - f(a))
            except ZeroDivisionError:
                return "Error: Division by zero encountered in method"

            # Перевірка збіжності
            if abs(f(x_new)) < accuracy:
                return f"Root: {x_new:.6f}, Iterations: {i + 1}, Precision: {accuracy}"

            # Оновлення проміжку
            a, b = b, x_new
        
        return "Method did not converge within the maximum number of iterations"