#!/usr/bin/env python3
"""
Module that delays
"""
import importlib, asyncio
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function takes one argument max_delay and
    returns an instance from the class asyncio.Task

    Args:
        max_delay: int
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
