#!/usr/bin/env python
"""
Module of the function
"""
import importlib
import asyncio
import typing
import random
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension():
    """
    Async comprehension
    """
    return [i async for i in async_generator()]
