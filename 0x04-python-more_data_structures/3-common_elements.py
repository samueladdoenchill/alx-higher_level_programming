#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Find the common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: New set containing elements that are common to both input sets.
    """
    return set_1 & set_2
