#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Initialize a variable to store the sum of unique integers
    sum_unique = 0

    # Iterate over the elements in my_list
    for element in my_list:
        # Check if the element is not in the unique_set
        if element not in unique_set:
            # Add the element to the set
            unique_set.add(element)
            # Add the element to the sum_unique
            sum_unique += element

    return sum_unique
