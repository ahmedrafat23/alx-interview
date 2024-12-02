#!/usr/bin/python3
"""
Module: island_perimeter
This module contains the function to calculate
the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Args:
        grid (list of list of ints): A 2D list where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If it's land
                perimeter += 4  # Start with 4 edges

                # Check if the cell above is land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract shared edge
                
                # Check if the cell to the left is land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract shared edge

    return perimeter
