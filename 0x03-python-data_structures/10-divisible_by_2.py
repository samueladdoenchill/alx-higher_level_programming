#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Determine divisibility by 2 for each element in the list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        A new list of booleans indicating whether element is divisible by 2.
    """
    if not my_list:
        return
    result_list = []
    for value in my_list:
        if value % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
