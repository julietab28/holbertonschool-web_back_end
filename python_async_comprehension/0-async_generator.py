#!/usr/bin/env python3
"""
Module of the function
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Function that returns a list of random numbers
    between 0 and 10
    """
    async for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
