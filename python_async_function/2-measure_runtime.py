#!/usr/bin/env python3
"""
This module provides a function to measure the average execution
time of the wait_n coroutine.
"""

import time
import asyncio
from typing import float
from wait_n import wait_n


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
    
    # Run the async function using asyncio.run()
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    
    return total_time / n
