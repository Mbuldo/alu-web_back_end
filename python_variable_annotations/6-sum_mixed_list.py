#!/usr/bin/env python3
"""Module containing a type-annotated function that sums a list of mixed numbers."""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
   """Return the sum of a list of integers and floats.

   Args:
       mxd_lst (List[Union[int, float]]): The list of ints and floats to sum

   Returns:
       float: The sum of all numbers in mxd_lst
   """
   return float(sum(mxd_lst))
