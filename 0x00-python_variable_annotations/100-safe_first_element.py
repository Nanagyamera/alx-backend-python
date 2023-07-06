#!/usr/bin/env python3
"""
task 10's module
"""
from typing import Optional, Any

def safe_first_element(lst: Optional[list]) -> Any:
    """
    correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
