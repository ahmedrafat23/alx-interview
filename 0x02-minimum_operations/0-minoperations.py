#!/usr/bin/python3
"""
This module calculates the minimum number of operations required
to result in exactly n 'H' characters using only Copy All and Paste.
"""

def minOperations(n):
    """
    Returns the minimum number of operations to get exactly n 'H' characters.
    
    If n is impossible to achieve or is less than 1, return 0.
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

