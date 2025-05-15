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

