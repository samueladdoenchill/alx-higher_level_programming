#!/usr/bin/python3

def magic_calculation(a, b, c):
    """
    Perform a magic calculation based on the given values.

    :param a: First input value.
    :param b: Second input value.
    :param c: Third input value.
    :return: Result of the magic calculation.
    """
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c
