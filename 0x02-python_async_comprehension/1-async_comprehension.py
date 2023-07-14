#!/usr/bin/env python3
"""
Task 1's module
"""
from typing import List
import asyncio
import random

async def async_generator() -> float:
    """
    Collects and returns 10 random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10

async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 numbers from a 10-number generator.
    """
    result = [number async for number in async_generator()]
    return result
