#!/usr/bin/env python3
"""Module with function that safely returns first element of sequence."""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): The sequence to get first element from

    Returns:
        Union[Any, None]: First element of sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None
