#!/usr/bin/env python3
"""Module containing a type-annotated function for list length calculations."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing sequences and their lengths.

    Args:
        lst (Iterable[Sequence]): List of sequences to measure

    Returns:
        List[Tuple[Sequence, int]]: List of tuples with sequences and lengths
    """
    return [(i, len(i)) for i in lst]
