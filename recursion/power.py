def power(N: int, M: int) -> int | float:
    """Return N to the power of M."""
    return power_recursive(N, M, 1)


def power_recursive(N: int, M: int, product: int | float) -> int | float:
    """Return N to the power of M."""
    if M == 0:
        return product
    if M < 0:
        product *= 1 / N
        M += 1
    else:
        product *= N
        M -= 1
    return power_recursive(N, M, product)
