#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Calculate the sum of unique elements in a list.

    Args:
        my_list (list): List of integers.

    Returns:
        int: Sum of unique elements in the list.
    """
    add = 0
    for element in set(my_list):
        add += element
    return add
