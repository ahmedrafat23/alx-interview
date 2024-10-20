#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of size n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        List of lists of integers.
    """
    if n <= 0:
        return []
    
    # The first row
    triangle = [[1]]

    # Construct the remaining rows
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle

