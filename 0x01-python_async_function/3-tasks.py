#!/usr/bin/env python3
"""
Task 3's module
"""
import asyncio
from basic_async_syntax import wait_random  # Importing wait_random from the previous file


def task_wait_random(max_delay):
    """
    Creates an asynchronous task for wait_random
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
