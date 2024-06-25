from typing import Any


def print_even_indexes(l: list[Any]) -> None:
    """Print elements on even indexes."""
    return print_even_indexes_recursive(l, 0)


def print_even_indexes_recursive(l: list[Any], i: int) -> None:
    """Print elements on even indexes."""
    if i >= len(l):
        return None
    print(l[i])
    return print_even_indexes_recursive(l, i + 2)
