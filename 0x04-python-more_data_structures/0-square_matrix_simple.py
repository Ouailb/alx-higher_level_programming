#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Initialize a new row for the new matrix
        new_row = []

        # Iterate over each element in the current row
        for element in row:
            # Square the element and append it to the new row
            new_row.append(element ** 2)

        # Append the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix
