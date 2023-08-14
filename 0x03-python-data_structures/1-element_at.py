#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Get the element at the specified index from the list.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at specified index if index is within valid range,
        otherwise, returns None.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
