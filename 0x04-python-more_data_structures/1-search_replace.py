#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate over the elements in my_list
    for element in my_list:
        # If the current element is equal to 'search', append 'replace' to the new list
        if element == search:
            new_list.append(replace)
        else:
            # Otherwise, append the current element to the new list
            new_list.append(element)

    return new_list
