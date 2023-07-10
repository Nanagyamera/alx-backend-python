#!/usr/bin/env python3
"""
Task 4's module
"""
import asyncio
from typing import List
from previous_file import task_wait_random  # Importing task_wait_random from the previous file


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
