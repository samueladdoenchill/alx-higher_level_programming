#!/usr/bin/python3

# Define a function named safe_function that takes
# a function (fct) and its arguments (*args).
# This function attempts to call the given function with
# the provided arguments and returns its result.
# If any exception occurs during the function call, the exception
# message is printed to stderr.
# Returns:
# - The result of the function call if successful, otherwise None
def safe_function(fct, *args):
    try:
        function_result = fct(*args)
        return function_result
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
