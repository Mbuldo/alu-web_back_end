#!/usr/bin/env python3
"""
This module provides a coroutine that collects random numbers using
async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: The list of 10 random numbers.
    """
    return [number async for number in async_generator()]
