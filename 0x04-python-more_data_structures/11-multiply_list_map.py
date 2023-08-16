#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in a list by a given number using map.

    Args:
        my_list (list): The list containing elements to be multiplied.
        number: The number to multiply each element by.

    Returns:
        list: A new list containing the elements of 'my_list'
        multiplied by 'number'.
    """
    return list(map((lambda x: x * number), my_list))
