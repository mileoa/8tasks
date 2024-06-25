from typing import Any


def list_len(l: list[Any]) -> int:
    """Return lenght of list."""
    return list_len_recursive(l, 0)


def list_len_recursive(l: list[Any], summ: int) -> int:
    """Return lenght of list."""
    if len(l) == 0:
        return summ
    l.pop(0)
    return list_len_recursive(l, summ + 1)
