#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of value-weight pairs.

    Args:
        my_list (list of tuples): List of tuples where tuple contains a value
            and its corresponding weight.

    Returns:
        float: The weighted average of values in list, or 0 if list is empty.
    """
    total_weighted_sum = 0
    total_weight = 0

    if len(my_list) == 0:
        return total_weighted_sum

    for item in my_list:
        total_weighted_sum += (item[0] * item[1])
        total_weight += item[1]

    return (total_weighted_sum / total_weight)
