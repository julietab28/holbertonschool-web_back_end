#!/usr/bin/env python3
"""
Module documentation
"""
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """
    THis function takes one argument and returns 
    a random number between 0 and 10

    Args: 
        max_delay: int
    """
    delay = random.randrange(0, max_delay)
    await asyncio(delay)
    return delay
