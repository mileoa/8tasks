def sum_digits(N: int) -> int:
    """Return sum of digits."""
    if N == 0:
        return 0
    return N % 10 + sum_digits(N // 10)
