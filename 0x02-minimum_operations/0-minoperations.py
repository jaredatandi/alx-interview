#!/usr/bin/env python3
"""A module to find min operations

Returns:
_type_: _description_
"""
import math
from typing import List


def minOperations(n):
    """Get the most number

    Args:
        n (_type_): number of times
    """


def minOperations(n: int) -> int:
    """find min operations

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    if n == 1:
        return 0

    # Find all factors of n
    factors: List[int] = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    # Calculate minimum operations for each factor
    min_ops: int = sum(factors)

    return min_ops
