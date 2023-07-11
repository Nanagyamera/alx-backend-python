#!/usr/bin/env python3
"""
Task 1's module
"""
import asyncio
import random


async def async_comprehension() -> List[float]:
    """
    collect and return 10 random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10

async def async_comprehension():
    result = [number async for number in async_generator()]
    return result
