#!/usr/bin/python3

# Define a function named raise_exception_msg that raises
# a NameError with an optional message
# Parameters:
# - message (str): Optional message to be associated with the NameError
def raise_exception_msg(message=""):
    raise NameError(message)
