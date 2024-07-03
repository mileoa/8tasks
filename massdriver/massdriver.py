def massdriver(activate: list[int]) -> int:
    """Return index of first occurance of value that occur >= 2 times."""
    return massdriver_recursive(activate, 0, {}, -1)


def massdriver_recursive(
    activate: list[int], i: int, history: dict[int, int], result: int
) -> int:
    """Return index of first occurance of value that occur >= 2 times."""
    if i == len(activate):
        return result
    if activate[i] not in history:
        history[activate[i]] = i
    else:
        if result > history[activate[i]] or result == -1:
            result = history[activate[i]]
    return massdriver_recursive(activate, i + 1, history, result)
