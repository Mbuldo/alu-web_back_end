#!/usr/bin/env python3
"""Module with function that zooms in on array elements."""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with each element repeated based on factor.

    Args:
        lst (Tuple): The input tuple to zoom
        factor (int): The number of times to repeat each element

    Returns:
        List: The zoomed list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
