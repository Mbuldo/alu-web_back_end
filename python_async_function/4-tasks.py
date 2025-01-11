#!/usr/bin/env python3
"""
This module provides an asynchronous routine that spawns task_wait_random
n times with a specified max_delay and returns the delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the
    specified max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []

    async def gather_delay() -> None:
        """
        Helper coroutine to get delay and insert it in sorted position.
        """
        task = task_wait_random(max_delay)
        delay = await task
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
