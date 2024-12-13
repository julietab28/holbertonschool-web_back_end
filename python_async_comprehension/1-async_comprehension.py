#!/usr/bin/env python
"""
"""
import importlib
import asyncio
import typing
import random
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension():
    return [i async for i in async_generator()]
