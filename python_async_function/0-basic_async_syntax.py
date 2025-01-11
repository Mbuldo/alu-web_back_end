#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for a random
amount of time between 0 and a specified maximum delay.
"""

import random
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds (inclusive) and returns the delay.

    Args:
        max_delay (int): The maximum delay time in seconds. Defaults to 10.

    Returns:
        float: The random delay time that was waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
