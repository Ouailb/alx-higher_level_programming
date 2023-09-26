#!/usr/bin/python3
'''def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print(my_list[count], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
'''
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()  # Add a newline after printing the elements
        return count
    except IndexError:
        print()  # Add a newline if an IndexError occurs
        return count
