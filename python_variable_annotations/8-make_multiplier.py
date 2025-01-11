#!/usr/bin/env python3
"""Module containing a type-annotated function for creating multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The number to multiply by

    Returns:
        Callable[[float], float]: A function that multiplies by multiplier
    """
    return lambda x: x * multiplier
