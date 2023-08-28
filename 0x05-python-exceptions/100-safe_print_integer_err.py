#!/usr/bin/python3

# Define a function named safe_print_integer_err that
# takes one argument:
# value (any type, but expected to be an integer)
# This function attempts to print the given value as an integer.
# If a ValueError or TypeError occurs, it prints the exception
# message to stderr.
# Returns:
# - True if the value is printed successfully, otherwise False
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
