#!/usr/bin/env python3
"""
task 3's module
"""
import time
from concurrent_execution import wait_n  # Importing wait_n from the previous file


def measure_time(n, max_delay):
    """
    the average runtime of wait_n
    """
    start_time = time.time()

    delays = wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
