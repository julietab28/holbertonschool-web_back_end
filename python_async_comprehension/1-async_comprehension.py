#!/usr/bin/env python3
"""
Module of the function
"""
import importlib
import asyncio
from typing import List
import random
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension
    """
    return [i async for i in async_generator()]
