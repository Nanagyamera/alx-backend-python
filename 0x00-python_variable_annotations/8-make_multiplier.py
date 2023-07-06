#!/usr/bin/env python3


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(number: float) -> float:
        return number * multiplier
    return multiplier_function
