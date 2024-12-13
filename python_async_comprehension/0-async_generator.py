#!/usr/bin/env python3
"""
"""
import asyncio
import random


async def async_generator():
    """
    Function that returns a list of random numbers
    between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
