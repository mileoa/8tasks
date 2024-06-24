from typing import Any


def list_len(l: list[Any]) -> int:
    """Return lenght of list."""
    try:
        l.pop(0)
        return 1 + list_len(l)
    except IndexError:
        return 0
