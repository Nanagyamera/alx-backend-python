#!/usr/bin/env python3
"""
task 8's module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
