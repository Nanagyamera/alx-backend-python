#!/usr/bin/env python3
"""
Task 1's module
"""
import asyncio
from random_delay import wait_random  # Importing wait_random from the previous file


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(tasks)
    delays = [task.result() for task in completed_tasks]
    delays.sort()  # Sort the list of delays in ascending order
    return delays
