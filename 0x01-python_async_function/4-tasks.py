#!/usr/bin/env python3
"""
Task 4's module
"""
import asyncio
from basic_async_syntax import wait_random, task_wait_random  # Importing wait_random and task_wait_random from the previous file

async def task_wait_n(n, max_delay):
    """
    computes task_wait_random n times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(tasks)
    delays = [task.result() for task in completed_tasks]
    delays.sort()  # Sort the list of delays in ascending order
    return delays
