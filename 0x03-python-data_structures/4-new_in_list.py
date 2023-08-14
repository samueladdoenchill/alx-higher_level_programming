#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Create a new list with an element replaced at the specified index.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The element to be placed at the specified index.

    Returns:
        A new list with the element replaced, or the original list if the index
        is out of bounds.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    modified_list = my_list[:]
    modified_list[idx] = element
    return modified_list
