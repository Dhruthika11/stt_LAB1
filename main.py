"""
This module contains various functions for simple mathematical
and string operations.
"""


def say_hi(name):
    """Returns a greeting for the given name."""
    return f"Hi, {name}."


def add(x, y):
    """Returns the sum of two numbers."""
    return x + y


def algebra(x, y):
    """
    Performs a specific algebraic calculation on two numbers.
    """
    return (x * y) * (x + y) * (x * x)


def say_bye(name):
    """Returns a farewell message."""
    return f"Bye, {name}."


def subtract(x, y):
    """Returns the difference between two numbers."""
    return x - y


def greater(x, y):
    """Returns True if the first number is greater than the second."""
    return x > y


def lesser(x, y):
    """Returns True if the first number is less than the second."""
    return x < y


print("Iam writing this code for the second task of the assignment.")
print(say_hi("Dhruthika"))
print(add(4, 13))
print(algebra(11, 2))
print(add(14, 3))
print(algebra(10, 4))
print(add(14, -10))
print(algebra(3, 5))
print(add(7, 3))
print(algebra(8, 2))
print(greater(14, -10))
print(greater(3, 5))
print(greater(7, 3))
print(greater(8, 2))
print(lesser(14, -10))
print(lesser(3, 5))
print(lesser(7, 3))
print(lesser(8, 2))
print(say_bye("Dhruthika"))
