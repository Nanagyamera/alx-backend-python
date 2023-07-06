#!/usr/bin/env python3
"""
task 11's module
"""
from typing import Dict, Any


def safely_get_value(dct: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """
    adding type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
