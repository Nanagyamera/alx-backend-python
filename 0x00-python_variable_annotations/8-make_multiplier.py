#!/usr/bin/env python3
"""
task 8's module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(number: float) -> float:
        return number * multiplier
    """
    function that multiplies a float by multiplier
    """
    return multiplier_function
