def EEC_help(arr1: list[int], arr2: list[int]) -> bool:
    """Return whether arr1 contain same elements as arr2."""
    return EEC_help_recursive(arr1, arr2, 0, {})


def EEC_help_recursive(
    arr1: list[int], arr2: list[int], i: int, arr_calc: dict[int, int]
) -> bool:
    """Return whether arr1 contain same elements as arr2."""
    if len(arr1) != len(arr2):
        return False
    if i == len(arr1):
        if list(arr_calc.values()).count(0) != len(arr_calc):
            return False
        return True

    if arr1[i] in arr_calc:
        arr_calc[arr1[i]] += 1
    else:
        arr_calc[arr1[i]] = 1

    if arr2[i] in arr_calc:
        arr_calc[arr2[i]] -= 1
    else:
        arr_calc[arr2[i]] = -1

    return EEC_help_recursive(arr1, arr2, i + 1, arr_calc)
