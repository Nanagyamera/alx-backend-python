#!/usr/bin/env python3
"""
Task 2's module
"""
import asyncio
import time
from previous_file import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures
    the total execution time
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    runtime = end_time - start_time
    return runtime
