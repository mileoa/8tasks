def print_even_elements(l: list[int]) -> None:
    """Print even elemnts."""
    return print_even_elements_recursive(l, 0)


def print_even_elements_recursive(l: list[int], i: int) -> None:
    """Print even elemnts."""
    if len(l) == i:
        return None
    if l[i] % 2 == 0:
        print(l[i])
    return print_even_elements_recursive(l, i + 1)
