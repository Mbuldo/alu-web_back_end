#!/usr/bin/env python3
"""Module with function for safely getting dictionary values."""


from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to get value from
        key (Any): The key to look up
        default (Union[T, None]): Default value to return if key not found

    Returns:
        Union[Any, T]: Value from dictionary or default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
