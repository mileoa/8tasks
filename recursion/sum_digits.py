def sum_digits(N: int) -> int:
    """Return sum of digits."""
    return sum_digits_recursive(N, 0)


def sum_digits_recursive(N: int, result: int) -> int:
    """Return sum of digits."""
    if N == 0:
        return result
    return sum_digits_recursive(N // 10, result + N % 10)
