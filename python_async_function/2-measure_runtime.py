#!/usr/bin/env python3
"""
This module provides a function to measure the average execution
time of the wait_n coroutine.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        float: Average execution time in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
