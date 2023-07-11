#!/usr/bin/env python3
"""
Taask 2's module
"""
import asyncio


from previous_file import async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times 
    in parallel using asyncio.gather
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
