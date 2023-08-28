#!/usr/bin/python3

# Define a function named safe_print_division
# that takes two arguments:
# a (numerator) and b (denominator) - both
# expected to be integers

def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
