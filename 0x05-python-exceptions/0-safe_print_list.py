#!/usr/bin/python3

# Define a function named safe_print_list
# that takes two arguments:
# my_list (a list containing any type of elements
# and x (number of elements to print)
def safe_print_list(my_list=[], x=0):
    count_printed = 0

    for index in range(x):
        try:
            print(my_list[index], end="")
            count_printed += 1
        except IndexError:
            break

    print()
    return count_printed
