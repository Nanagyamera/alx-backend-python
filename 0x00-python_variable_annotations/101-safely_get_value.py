#!/usr/bin/env python3
"""
task 11's module
"""
from typing import Dict, Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    adding type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
