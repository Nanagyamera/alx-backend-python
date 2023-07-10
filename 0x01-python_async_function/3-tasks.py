#!/usr/bin/env python3
"""
Task 3's module
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Computes the list of all the delays (float values)
    """
    return asyncio.create_task(wait_random(max_delay))
