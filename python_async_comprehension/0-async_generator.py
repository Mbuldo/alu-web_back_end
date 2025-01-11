#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random numbers
after waiting for a delay.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    after waiting for 1 second, repeated 10 times.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
