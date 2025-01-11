#!/usr/bin/env python3
"""Module containing a type-annotated function that sums a list of floats."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats to sum

    Returns:
        float: The sum of all floats in input_list
    """
    return sum(input_list)
