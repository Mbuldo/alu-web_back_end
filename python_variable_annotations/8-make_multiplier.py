#!/usr/bin/env python3
"""Module containing a type-annotated function that returns a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
   """Return a function that multiplies a float by multiplier.

   Args:
       multiplier (float): The multiplication factor

   Returns:
       Callable[[float], float]: A function that takes a float and returns float
   """
   return lambda x: x * multiplier
