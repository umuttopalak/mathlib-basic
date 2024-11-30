from typing import Union

from mathlib_basic.errors import DivideError


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts b from a.

    Parameters:
    a (int or float): The number to be subtracted from.
    b (int or float): The number to subtract.

    Returns:
    int or float: The result of a - b.
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies a and b.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of a and b.
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides a by b. Checks for division by zero.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    int or float: The result of a / b.

    Raises:
    DivideError: If b is zero.
    """
    if b == 0:
        raise DivideError("Error: cannot divide by zero!")
    return a / b
