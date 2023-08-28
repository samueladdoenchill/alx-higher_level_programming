#!/usr/bin/python3

# Define a function named list_division that takes three arguments:
# my_list_1 (a list containing numerical elements),
# my_list_2 (a list containing numerical elements),
# list_length (the number of elements to process)

def list_division(my_list_1, my_list_2, list_length):
    modified_list = []
    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            modified_list.append(result)
    return modified_list
