#!/usr/bin/env python3

"""
    Modulo del archivo
"""
import asyncio
import random


async def async_generator():
    
    #[i async for i in range(10) await asyncio.sleep(1)]

    async for i in range(10):
        await asyncio.sleep(1)
        random.uniform(0, 10)
