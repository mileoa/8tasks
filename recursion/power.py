def power(N: int, M: int) -> int | float:
    """Return N to the power of M."""
    if M == 0:
        return 1
    if M < 0:
        return 1 / pow(N, -M)
    return N * pow(N, M - 1)
