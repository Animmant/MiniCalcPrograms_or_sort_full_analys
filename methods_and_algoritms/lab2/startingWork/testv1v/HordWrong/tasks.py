import math
from scipy.optimize import root_scalar, fixed_point

"""
TASK_DEFINITIONS = {
    "18": ("task_18", 1, str, "Example: Hello   world  python   code")  
}
"""

class TaskManager:
    def __init__(self):
        self.tasks = {
            "hord": (self.task_find_root_hord, 0, float),
            "methods": (self.task_find_root_methods, 0, float),
            "6.a": (self.task_6_a, 1, str), 
            "18": (self.task_18, 1, str)
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

 
    def task_6_a(self, variables):
        text = variables[0] if variables else "Hello world! How are you!"
        
        exclamation_index = text.find('!')
        if exclamation_index == -1:
            return "No exclamation mark found in the string", f"Input: {text}", 0
        
        spaces_count = text[:exclamation_index].count(' ')
        
        return "Count spaces before first exclamation mark", f"Input: {text}", spaces_count

    def text_split(self, text):
        return [word for word in text.split() if word]

    def task_18(self, variables):
        text = variables[0] if variables else "Hello world level deed stats"
        
        words = self.text_split(text)
        
        matching_words = [word for word in words if word and word[0].lower() == word[-1].lower()]
        
        result = {
            "total_words": len(words),
            "matching_words": matching_words,
            "matching_count": len(matching_words)
        }
        
        return ("Count words where first and last characters match", 
                f"Input: {text}", 
                f"Matching words: {matching_words}\nCount: {len(matching_words)}")
  
    def init_eq(self, x):
        return x + math.cos(x) - 1
    
    def task_find_root_hord(self, variables):
        if len(variables) < 2:
            a = -0.5
            b = 0.5
        else:
            a = variables[0]
            b = variables[1]
        
        result = self.find_root_hord(self, self.init_eq, a, b, 1e-3, 1000)
        
        return (
            "Finding root using Chord method", 
            f"Interval: [{a}, {b}]",
            result
        )
    
    def find_root_hord(self, f, a, b, accuracy=1e-3, max_iterations=1000):
        if f(a) * f(b) >= 0:
            return "No root found in the interval"

        # Ініціалізуємо x_new перед циклом
        x_new = a  # початкове значення
        
        for current_iter in range(max_iterations):
            fa, fb = f(a), f(b)

            # Prevent division by zero
            if abs(fb - fa) < 1e-10:
                return "Error: Function values at a and b are too close, division by zero risk."

            # Compute new approximation
            x_new = a - fa * (b - a) / (fb - fa)

            # Check for convergence
            if abs(f(x_new)) < accuracy:
                return {
                    "status": "success",
                    "value": x_new,
                    "iterations": current_iter + 1  # Додаємо 1, щоб показати реальну кількість ітерацій
                }

            # Update interval correctly
            if fa * f(x_new) < 0:
                b = x_new  # Keep `a`, move `b`
            elif fb * f(x_new) < 0:
                a = x_new  # Keep `b`, move `a`
            else:
                return {
                    "status": "failed",
                    "last_x": x_new,
                    "reason": "Function did not change sign - method may not be applicable"
                }

        return {
            "status": "failed",
            "last_x": x_new,
            "reason": "Method did not converge within max iterations"
        }

    
    def task_find_root_methods(self, variables):
        a, b = (-0.5, 0.5) if len(variables) < 2 else (float(variables[0]), float(variables[1]))
        accuracy = 1e-3  # Precision level for root finding
        
        # Ensure the function has a root in the given interval
        if self.init_eq(a) * self.init_eq(b) >= 0:
            return "No root found in the interval"

        methods = {
            "Chord": {"method": "secant", "x0": a, "x1": b, "xtol": accuracy},
            "Newton": {"method": "newton", "x0": b, "fprime": lambda x: 1 - math.sin(x), "xtol": accuracy},
            "Brentq": {"method": "brentq", "bracket": (a, b), "xtol": accuracy},  # `bracket` required instead of `a, b`
            "Bisection": {"method": "bisect", "bracket": (a, b), "xtol": accuracy},  # Similar to `brentq`
        }

        results = {}

        for name, params in methods.items():
            try:
                result = root_scalar(self.init_eq, **params, maxiter=100)
                if not result.converged:
                    results[name] = "Did not converge within 100 iterations"
                else:
                    results[name] = f"Root: {result.root:.6f}, Iterations: {result.iterations}, Precision: {accuracy}"
            except ValueError as e:
                results[name] = f"Error: {str(e)}"
            except Exception as e:
                results[name] = f"Unexpected Error: {str(e)}"

        # Fixed-point iteration must be handled separately, as `root_scalar` does not support it
        try:
            fixed_point_root = fixed_point(lambda x: 1 - math.cos(x), b, xtol=accuracy)
            results["Fixed-Point Iteration"] = f"Root: {fixed_point_root:.6f}, Precision: {accuracy}"
        except Exception as e:
            results["Fixed-Point Iteration"] = f"Error: {str(e)}"

        return "Root finding methods", f"Interval: [{a}, {b}]", results
