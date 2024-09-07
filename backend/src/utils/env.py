import os
from typing import TypeVar, cast

T = TypeVar("T")

def value_or_error(key: str, default: T | None = None) -> T:
    value = os.getenv(key)
    
    if value is None and default is not None:
        return default
    
    if value is None:
        raise ValueError(f"Env missing required key {key}")
    
    return cast(T, value)
    

        