#!/usr/bin/env python3
"""Module that contains a type-annotated function for string concatenation."""


def concat(str1: str, str2: str) -> str:
    """Return the concatenation of two strings.

    Args:
        str1 (str): First string to concatenate
        str2 (str): Second string to concatenate

    Returns:
        str: The concatenation of str1 and str2
    """
    return str1 + str2
