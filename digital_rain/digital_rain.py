def digital_rain(col: str) -> str:
    """Return longest substring with equal 1 and 0 chars."""
    return digital_rain_recursive(col, 0, 0, 0, 0, "", {0: -1})


def digital_rain_recursive(
    col: str,
    i: int,
    count_0: int,
    count_1: int,
    max_len: str,
    max_str: str,
    difference: dict,
) -> str:
    """Return longest substring with equal 1 and 0 chars."""
    if i == len(col):
        return max_str

    if col[i] == "0":
        count_0 += 1
    else:
        count_1 += 1

    diff: int = count_0 - count_1
    if diff in difference:
        start: int = difference[diff]
        end: int = i
        current_len: int = end - start
        if current_len >= max_len:
            max_len = current_len
            max_str = col[start + 1 : end + 1]
    else:
        difference[diff] = i

    return digital_rain_recursive(
        col, i + 1, count_0, count_1, max_len, max_str, difference
    )
