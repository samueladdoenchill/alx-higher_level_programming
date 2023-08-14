#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of 'c' and 'C' from the given string.

    Args:
        my_string (str): The input string from which to remove 'c' and 'C'.

    Returns:
        A new string with 'c' and 'C' characters removed.
    """
    chars_to_remove = "cC"
    result_string = ""
    for char in my_string:
        if char not in chars_to_remove:
            result_string += char
    return result_string
