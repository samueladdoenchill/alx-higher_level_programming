#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace element at specified index in list with given element.

    Args:
        my_list (list): The list in which to perform the replacement.
        idx (int): The index at which to replace the element.
        element: The element to be placed at the specified index.

    Returns:
        The modified list after replacement, or original list if index
        is out of bounds.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
