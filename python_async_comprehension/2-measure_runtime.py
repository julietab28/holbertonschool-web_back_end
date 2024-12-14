#!/usr/bin/env python3
"""
Module of the function
"""
import asyncio
import importlib
import time
async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Function tahat returns the total time to complete
    all the tasks
    """
    start = time.perf_counter()
    task1 = asyncio.create_task(async_comprehension())
    task2 = asyncio.create_task(async_comprehension())
    task3 = asyncio.create_task(async_comprehension())
    task4 = asyncio.create_task(async_comprehension())
    tasks = (task1, task2, task3, task4)
    await asyncio.gather(*tasks)
    end = time.perf_counter()

    total_time = end - start

    return total_time
