#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise and return the result.

    Args:
        tuple_a (tuple): The first tuple to be added.
        tuple_b (tuple): The second tuple to be added.

    Returns:
        A new tuple containing the element-wise sum of the input tuples.
    """
    if len(tuple_a) == 0:
        a_val = 0
        b_val = 0
    elif len(tuple_a) == 1:
        a_val = tuple_a[0]
        b_val = 0
    else:
        a_val = tuple_a[0]
        b_val = tuple_a[1]

    if len(tuple_b) == 0:
        c_val = 0
        d_val = 0
    elif len(tuple_b) == 1:
        c_val = tuple_b[0]
        d_val = 0
    else:
        c_val = tuple_b[0]
        d_val = tuple_b[1]

    new_tuple = (a_val + c_val, b_val + d_val)
    return new_tuple
