from scipy.optimize import root_scalar, fixed_point
import math
import time

class TaskManager:
    def __init__(self):
        self.tasks = {
            "methods": (self.task_find_root_methods, 0, float),
            "hord": (self.task_find_root_hord, 0, float),
            "newton": (self.task_find_root_newton, 0, float),
            "combined": (self.task_find_root_combined, 0, float),
            "bisection": (self.task_find_root_bisection, 0, float),
            "fixed_point": (self.task_find_root_fixed_point, 1, float)
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
        accuracy = 1e-2  
        
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
    
    def task_find_root_newton(self, variables):
        """
        Task handler for Newton's method.
        
        Args:
            variables: List of input values from UI
            
        Returns:
            Tuple with description, input data, and result
        """
        if len(variables) < 1:
            x0 = 0.5  # Default initial approximation
        else:
            x0 = float(variables[0])
        
        print(f"Using initial approximation: {x0}")
        
        # Define the derivative of init_eq (x + cos(x) - 1)
        def derivative(x):
            return 1 - math.sin(x)
        
        result = self.find_root_newton(self.init_eq, derivative, x0, 1e-3, 100)
        
        if isinstance(result, dict) and result["status"] == "success":
            formatted_result = f"Root: {result['value']:.6f}, Iterations: {result['iterations']}, Precision: {result['precision']}"
        else:
            formatted_result = result
        
        return (
            "Finding root using Newton's method",
            f"Initial approximation: {x0}",
            formatted_result
        )

    def find_root_newton(self, f, df, x0, accuracy=1e-3, max_iterations=100):
        """
        Find root using Newton's method.
        
        Args:
            f: Function whose root we seek
            df: Derivative of the function
            x0: Initial approximation
            accuracy: Desired precision
            max_iterations: Maximum number of iterations
            
        Returns:
            Dictionary with status, value, iterations, and precision
        """
        x = x0
        
        for i in range(max_iterations):
            fx = f(x)
            
            # Check if we've already found a root
            if abs(fx) < accuracy:
                return {
                    "status": "success",
                    "value": x,
                    "iterations": i,
                    "precision": accuracy
                }
            
            dfx = df(x)
            
            # Prevent division by zero
            if abs(dfx) < 1e-10:
                return {
                    "status": "error",
                    "reason": "Derivative too close to zero",
                    "value": x,
                    "iterations": i
                }
            
            # Newton's formula
            x_new = x - fx / dfx
            
            # Check for convergence
            if abs(x_new - x) < accuracy:
                return {
                    "status": "success",
                    "value": x_new,
                    "iterations": i + 1,
                    "precision": accuracy
                }
            
            x = x_new
        
        # If we reach here, the method didn't converge
        return {
            "status": "failed",
            "reason": "Method did not converge within maximum iterations",
            "value": x,
            "iterations": max_iterations
        }

    def task_find_root_combined(self, variables):
        """
        Task handler for Combined method (Chord-Newton).
        
        Args:
            variables: List of input values from UI
            
        Returns:
            Tuple with description, input data, and result
        """
        if len(variables) < 2:
            a, b = -0.5, 0.5
        else:
            a, b = float(variables[0]), float(variables[1])
        
        print(f"Using interval: [{a}, {b}]")
        
        # Define the derivative of init_eq (x + cos(x) - 1)
        def derivative(x):
            return 1 - math.sin(x)
        
        result = self.find_root_combined(self.init_eq, derivative, a, b, 1e-3, 100)
        
        if isinstance(result, dict) and result["status"] == "success":
            formatted_result = f"Root: {result['value']:.6f}, Iterations: {result['iterations']}, Precision: {result['precision']}"
        elif isinstance(result, dict):
            formatted_result = f"{result['status'].capitalize()}: {result.get('reason', '')}, Value: {result.get('value', 'N/A')}"
        else:
            formatted_result = result
        
        return (
            "Finding root using Combined method",
            f"Interval: [{a}, {b}]",
            formatted_result
        )

    def find_root_combined(self, f, df, a, b, accuracy=1e-3, max_iterations=100):
        """
        Find root using Combined method (alternating between Chord and Newton).
        
        Args:
            f: Function whose root we seek
            df: Derivative of the function
            a, b: Initial interval bounds
            accuracy: Desired precision
            max_iterations: Maximum number of iterations
            
        Returns:
            Dictionary with status, value, iterations, and precision
        """
        # Check if there's a root in the interval
        if f(a) * f(b) >= 0:
            return {
                "status": "error",
                "reason": "No root in the given interval or method unsuitable",
                "value": None,
                "iterations": 0
            }
        
        # Determine which endpoint to use for Newton's method
        # We choose the point where f(x) and f''(x) have the same sign
        # This is a heuristic to ensure Newton's method converges monotonically
        fa, fb = f(a), f(b)
        
        # Use numerical approximation for second derivative
        h = 1e-5
        f_second_a = (df(a + h) - df(a)) / h
        f_second_b = (df(b + h) - df(b)) / h
        
        # Choose initial point for Newton's method
        if fa * f_second_a > 0:
            x_newton = a
        else:
            x_newton = b
        
        total_iterations = 0
        
        for i in range(max_iterations):
            # Step 1: Apply chord method to get a new approximation
            try:
                chord_new = b - (f(b) * (b - a)) / (f(b) - f(a))
            except ZeroDivisionError:
                return {
                    "status": "error",
                    "reason": "Division by zero in chord method",
                    "value": None,
                    "iterations": total_iterations
                }
            
            total_iterations += 1
            
            # Check convergence after chord step
            if abs(f(chord_new)) < accuracy:
                return {
                    "status": "success",
                    "value": chord_new,
                    "iterations": total_iterations,
                    "precision": accuracy
                }
            
            # Update interval for chord method
            a, b = b, chord_new
            
            # Step 2: Apply Newton's method to refine the approximation
            fx = f(x_newton)
            dfx = df(x_newton)
            
            # Prevent division by zero
            if abs(dfx) < 1e-10:
                return {
                    "status": "error",
                    "reason": "Derivative too close to zero in Newton step",
                    "value": x_newton,
                    "iterations": total_iterations
                }
            
            # Newton's formula
            newton_new = x_newton - fx / dfx
            total_iterations += 1
            
            # Check convergence after Newton step
            if abs(f(newton_new)) < accuracy:
                return {
                    "status": "success",
                    "value": newton_new,
                    "iterations": total_iterations,
                    "precision": accuracy
                }
            
            # Update Newton point
            x_newton = newton_new
            
            # Additional convergence check
            if abs(chord_new - newton_new) < accuracy:
                # Return the more accurate of the two approximations
                if abs(f(chord_new)) < abs(f(newton_new)):
                    return {
                        "status": "success",
                        "value": chord_new,
                        "iterations": total_iterations,
                        "precision": accuracy
                    }
                else:
                    return {
                        "status": "success",
                        "value": newton_new,
                        "iterations": total_iterations,
                        "precision": accuracy
                    }
        
        # If we reach here, the method didn't converge
        # Return the better of the two approximations
        if abs(f(chord_new)) < abs(f(newton_new)):
            final_value = chord_new
        else:
            final_value = newton_new
        
        return {
            "status": "failed",
            "reason": "Method did not converge within maximum iterations",
            "value": final_value,
            "iterations": total_iterations
        }

    def task_find_root_bisection(self, variables):
        """
        Task handler for Bisection method.
        
        Args:
            variables: List of input values from UI
            
        Returns:
            Tuple with description, input data, and result
        """
        if len(variables) < 2:
            a, b = -0.5, 0.5
        else:
            a, b = float(variables[0]), float(variables[1])
        
        print(f"Using interval: [{a}, {b}]")
        
        result = self.find_root_bisection(self.init_eq, a, b, 1e-3, 100)
        
        if isinstance(result, dict) and result["status"] == "success":
            formatted_result = f"Root: {result['value']:.6f}, Iterations: {result['iterations']}, Precision: {result['precision']}"
        elif isinstance(result, dict):
            formatted_result = f"{result['status'].capitalize()}: {result.get('reason', '')}, Value: {result.get('value', 'N/A')}"
        else:
            formatted_result = result
        
        return (
            "Finding root using Bisection method",
            f"Interval: [{a}, {b}]",
            formatted_result
        )

    def find_root_bisection(self, f, a, b, accuracy=1e-3, max_iterations=100):
        """
        Find root using Bisection method.
        
        Args:
            f: Function whose root we seek
            a, b: Initial interval bounds
            accuracy: Desired precision
            max_iterations: Maximum number of iterations
            
        Returns:
            Dictionary with status, value, iterations, and precision
        """
        # Check if there's a root in the interval
        fa, fb = f(a), f(b)
        if fa * fb >= 0:
            return {
                "status": "error",
                "reason": "No root in the given interval or multiple roots",
                "value": None,
                "iterations": 0
            }
        
        # If one of the endpoints is already a root, return it
        if abs(fa) < accuracy:
            return {
                "status": "success",
                "value": a,
                "iterations": 0,
                "precision": accuracy
            }
        
        if abs(fb) < accuracy:
            return {
                "status": "success",
                "value": b,
                "iterations": 0,
                "precision": accuracy
            }
        
        for i in range(max_iterations):
            # Calculate midpoint
            c = (a + b) / 2
            fc = f(c)
            
            # Check if we found the root
            if abs(fc) < accuracy:
                return {
                    "status": "success",
                    "value": c,
                    "iterations": i + 1,
                    "precision": accuracy
                }
            
            # Check if interval is small enough
            if (b - a) / 2 < accuracy:
                return {
                    "status": "success",
                    "value": c,
                    "iterations": i + 1,
                    "precision": (b - a) / 2
                }
            
            # Update interval
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        
        # If we reach here, the method didn't converge
        c = (a + b) / 2
        return {
            "status": "failed",
            "reason": "Method did not converge within maximum iterations",
            "value": c,
            "iterations": max_iterations
        }

    def task_find_root_fixed_point(self, variables):
        """
        Task handler for Fixed-Point Iteration method.
        
        Args:
            variables: List of input values from UI
            
        Returns:
            Tuple with description, input data, and result
        """
        if len(variables) < 1:
            x0 = 0.5  # Default initial approximation
        else:
            x0 = float(variables[0])
        
        print(f"Using initial approximation: {x0}")
        
        # Define the fixed-point function g(x) where x = g(x)
        # For equation x + cos(x) - 1 = 0, we rearrange to x = 1 - cos(x)
        def g(x):
            return 1 - math.cos(x)
        
        result = self.find_root_fixed_point(g, x0, 1e-3, 100)
        
        if isinstance(result, dict) and result["status"] == "success":
            formatted_result = f"Root: {result['value']:.6f}, Iterations: {result['iterations']}, Precision: {result['precision']}"
        elif isinstance(result, dict):
            formatted_result = f"{result['status'].capitalize()}: {result.get('reason', '')}, Value: {result.get('value', 'N/A')}"
        else:
            formatted_result = result
        
        return (
            "Finding root using Fixed-Point Iteration method",
            f"Initial approximation: {x0}",
            formatted_result
        )

    def find_root_fixed_point(self, g, x0, accuracy=1e-3, max_iterations=100):
        """
        Find root using Fixed-Point Iteration method.
        
        Args:
            g: Function in the form x = g(x)
            x0: Initial approximation
            accuracy: Desired precision
            max_iterations: Maximum number of iterations
            
        Returns:
            Dictionary with status, value, iterations, and precision
        """
        x = x0
        
        for i in range(max_iterations):
            # Compute next iteration
            x_new = g(x)
            
            # Check for convergence
            if abs(x_new - x) < accuracy:
                return {
                    "status": "success",
                    "value": x_new,
                    "iterations": i + 1,
                    "precision": accuracy
                }
            
            # Check if the method is diverging
            if i > 0 and abs(x_new - x) > abs(x - x_prev) * 2:
                return {
                    "status": "failed",
                    "reason": "Method is diverging - try a different transformation or initial point",
                    "value": x_new,
                    "iterations": i + 1
                }
            
            x_prev = x
            x = x_new
        
        # If we reach here, the method didn't converge
        return {
            "status": "failed",
            "reason": "Method did not converge within maximum iterations",
            "value": x,
            "iterations": max_iterations
        }
    
