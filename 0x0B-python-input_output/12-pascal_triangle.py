#!/usr/bin/python3
""" pascal """


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the result as an empty list of lists
    result = []

    for i in range(n):
        # Initialize a new row with the first element always being 1
        row = [1]

        # Calculate the values in the current row
        for j in range(1, i):
            # Each value is the sum of the two values from the previous row
            value = result[i - 1][j - 1] + result[i - 1][j]
            row.append(value)

        # Add the last element to the row, which is also always 1
        if i > 0:
            row.append(1)

        # Append the row to the result
        result.append(row)

    return result
