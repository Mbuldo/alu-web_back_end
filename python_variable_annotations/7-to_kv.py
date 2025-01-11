#!/usr/bin/env python3
"""Module containing a type-annotated function that returns a tuple."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and square of a number.

    Args:
        k (str): The string to be used as first element
        v (Union[int, float]): The number to be squared

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v
    """
    return (k, float(v ** 2))
