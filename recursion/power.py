def power(N: int, M: int) -> int | float:
    """Return N to the power of M."""
    if M < 0:
        return 1 / power_recursive(N, -M, 1)
    return power_recursive(N, M, 1)


def power_recursive(N: int, M: int, product: int | float) -> int | float:
    """Return N to the power of M."""
    if M == 0:
        return product
    return power_recursive(N, M - 1, product * N)
