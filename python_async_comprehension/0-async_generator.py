#!/usr/bin/env python3
"""
Module of the function
"""
import asyncio
import random
import time
from typing import Generator


def async_generator() -> Generator[float, NoneType, NoneType]:
    """
    Function that returns a list of random numbers
    between 0 and 10
    """
    for i in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)
