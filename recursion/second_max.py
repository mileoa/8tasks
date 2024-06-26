def second_max(l: list[int]) -> int:
    """Return second max value."""
    if l[0] > l[1]:
        return second_max_recursive(l, l[0], l[1], 2)
    return second_max_recursive(l, l[1], l[0], 2)


def second_max_recursive(l: list[int], max_1: int, max_2: int, i: int) -> int:
    """Return second max value."""
    if i == len(l):
        return max_2
    if l[i] >= max_1:
        max_2 = max_1
        max_1 = l[i]
    elif l[i] > max_2:
        max_2 = l[i]
    return second_max_recursive(l, max_1, max_2, i + 1)
