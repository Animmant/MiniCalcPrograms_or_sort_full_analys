# src/components/method_int.py
"""
Module for numerical integration methods.
This module provides functions for numerical approximation of definite integrals.
"""
import math

def func1_var10(x: float) -> float:
    """
    Calculates the value of the first function for variant 10.
    f(x) = 1 / sqrt(1 + 2*x^2).

    Args:
        x: The input value.

    Returns:
        The calculated value of the function.

    Raises:
        ValueError: If the denominator is zero (practically, 1 + 2*x^2 is always > 0).
    """
    denominator_sq_arg = 1 + 2 * x**2
    # This check is mostly for robustness, as 1 + 2*x^2 is always positive.
    if denominator_sq_arg <= 0:
        # This case should not be reached for real x.
        # If it were, sqrt would raise a ValueError.
        raise ValueError("Argument for sqrt must be positive in func1_var10.")
    
    denominator = math.sqrt(denominator_sq_arg)
    
    # This check is also mostly theoretical as denominator will be > 0.
    if denominator == 0:
        raise ValueError("Division by zero in func1_var10.")
    return 1 / denominator

def func2_var10(x: float) -> float:
    """
    Calculates the value of the second function for variant 10.
    f(x) = lg(x^2 + 0.5) / (1 + 2*x^2), where lg is the decimal logarithm (log10).

    Args:
        x: The input value.

    Returns:
        The calculated value of the function.

    Raises:
        ValueError: If the argument for log10 is not positive or if division by zero occurs.
    """
    numerator_arg = x**2 + 0.5
    if numerator_arg <= 0:
        raise ValueError("Argument for log10 must be positive in func2_var10.")
    
    numerator = math.log10(numerator_arg)
    
    denominator = 1 + 2 * x**2
    # Denominator 1 + 2*x^2 is always positive for real x.
    # This check is for completeness.
    if denominator == 0: 
        raise ValueError("Division by zero in func2_var10.")
    return numerator / denominator

def left_rectangle_method(func: callable, a: float, b: float, n: int) -> float:
    """
    Calculates the definite integral of a function using the left rectangle method.

    The formula used is: Integral(f(x)dx) from a to b approx = h * sum(f(x_i)) for i=0 to n-1,
    where h = (b-a)/n and x_i = a + i*h.
    This implementation correctly handles cases where a > b (h becomes negative).

    Args:
        func: The function to integrate. It should take a single float argument 
              and return a float.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of subintervals to use. Must be a positive integer.

    Returns:
        The approximate value of the definite integral.

    Raises:
        ValueError: If n is not a positive integer.
        TypeError: If func is not callable.
    """
    if not callable(func):
        raise TypeError("Input 'func' must be a callable function.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of intervals (n) must be a positive integer.")
    
    if a == b:
        return 0.0

    h = (b - a) / n
    integral_sum = 0.0

    for i in range(n):  # Sum from i=0 to n-1
        # x_i is the left endpoint of the k-th subinterval.
        # If h is negative (a > b), x_i sequence decreases from a.
        x_i = a + (i + 1) * h
        try:
            integral_sum += func(x_i)
        except ValueError as e:
            # Propagate errors from func (e.g., math domain error)
            raise ValueError(f"Error in function evaluation at x={x_i}: {e}") from e
            
    return h * integral_sum