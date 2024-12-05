#!/usr/bin/env python3
import importlib, asyncio
wait_random = importlib.import_module('0-basic_async_syntax').wait_random
"""
Module that delays
"""
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function takes two arguments and returns a List
    that contains n floats and are ordered asc

    Args:
        n: int
        max_delay: int
    """
    list_delay = []
    list_tareas = []
    for i in range(n):
        tarea = asyncio.create_task(wait_random(max_delay))
        list_tareas.append(tarea)

    for tarea in asyncio.as_completed(list_tareas):
        time = await tarea
        list_delay.append(time)

    return list_delay
