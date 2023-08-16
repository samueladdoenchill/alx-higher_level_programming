#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of a given element with another element in a list.

    Args:
        my_list (list): The original list to be modified.
        search: The element to be replaced.
        replace: The new element to replace 'search' with.

    Returns:
        list: Modified list where 'search' items are replaced with 'replace'.
    """
    modified_list = my_list.copy()
    for item in range(len(modified_list)):
        if modified_list[item] == search:
            modified_list[item] = replace
    return modified_list
