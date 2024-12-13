#!/usr/bin/env python3
"""
Module that sums
"""
import importlib, asyncio
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n
import time


async def measure_time(n: int, max_delay: int) -> float:
    """

    """
    tasks_copleted = []
    start = time.perf_counter()

    for i in range(n):
        task = asyncio.create_task(wait_n(n, max_delay))
        tasks_copleted.append(task)
    
    await asyncio.gather(*tasks_copleted)
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
