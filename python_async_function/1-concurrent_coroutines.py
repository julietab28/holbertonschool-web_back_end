#!/usr/bin/env python3
"""
Module that delays
"""
import importlib
import asyncio
from typing import List
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


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
