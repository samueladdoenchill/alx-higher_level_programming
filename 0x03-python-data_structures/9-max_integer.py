#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find and return the maximum integer in the given list.

    Args:
        my_list (list): The input list.

    Returns:
        The maximum integer in the list, or None if the list is empty.
    """
    if not my_list:
        return
    max_val = my_list[0]
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val
