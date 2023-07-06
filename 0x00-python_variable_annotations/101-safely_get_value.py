#!/usr/bin/env python3


from typing import Dict, Any

def safely_get_value(dct: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    if key in dct:
        return dct[key]
    else:
        return default
