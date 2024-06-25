from typing import Any


def list_len(l: list[Any]) -> int:
    """Return lenght of list."""
    if len(l) == 0:
        return 0
    l.pop(0)
    return 1 + list_len(l)
