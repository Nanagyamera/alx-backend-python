#!/usr/bin/env python3
"""
Task 0's module
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    waits for a random number of seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
