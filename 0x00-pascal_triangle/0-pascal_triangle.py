#!/usr/bin/python3

"""
This module contains a function for generating Pascal's triangle.Returns a
list of lists representing the Pascal's triangle of a given integer n.
"""


def pascal_triangle(n):

    """
    Generate Pascal's triangle up to the nth row

    """

    # Return an empty list if n is less than or equal to 0

    if n <= 0:
        return []

    # Initialize the triangle with the first row [1]
    triangle = [[1]]

    # Loop through the range to generate each row of Pascal's triangle
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Fill in the middle values by summing adjacent elements
        # from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with a 1
        row.append(1)
        # Append the newly created row to the triangle
        triangle.append(row)

    return (triangle)
