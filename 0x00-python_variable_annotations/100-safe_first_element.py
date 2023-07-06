#!/usr/bin/env python3
from typing import Optional, Any


def safe_first_element(lst: Optional[list]) -> Any:
    if lst:
        return lst[0]
    else:
        return None
