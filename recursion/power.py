def power(N: int, M: int) -> int | float:
    """Return N to the power of M."""
    M_negative: bool = M < 0
    if M_negative:
        M = -M
    return power_recursive(N, M, M_negative, 1)


def power_recursive(
    N: int, M: int, M_negative: bool, product: int | float
) -> int | float:
    """Return N to the power of M."""
    if M == 0:
        if M_negative:
            return 1 / product
        return product
    return power_recursive(N, M - 1, M_negative, product * N)
