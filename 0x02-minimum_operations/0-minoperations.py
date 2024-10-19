#!/usr/bin/python3
"""
This module calculates the minimum number of operations required
to result in exactly n 'H' characters using only Copy All and Paste.
"""


def min_operations(n):
    """
    Returns the minimum number of operations to get exactly n 'H' characters.
    
    If n is impossible to achieve or is less than 1, return 0.
    """
    if n <= 1:
        return 0  # No operations needed if n <= 1
    
    operations = 0  # This will hold the total number of operations
    divisor = 2  # Start checking with the smallest divisor, which is 2
    
    # Continue until we reduce n to 1 by dividing it by its divisors
    while n > 1:
        # If n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the count of operations
            n //= divisor  # Reduce n by dividing it by the divisor
        divisor += 1  # Move to the next divisor
    
    return operations  # Return the total number of operations needed

