#!/usr/bin/env python3
"""
This module provides an asynchronous routine that spawns wait_random n times
with a specified max_delay and returns the delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified
    max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []

    async def gather_delay() -> None:
        """
        Helper coroutine to get delay and insert it in sorted position.
        """
        delay = await wait_random(max_delay)
        # Insert delay in the correct position to maintain ascending order
        position = 0
        while position < len(delays) and delays[position] < delay:
            position += 1
        delays.insert(position, delay)

    # Create list of tasks
    tasks = [gather_delay() for _ in range(n)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    return delays
