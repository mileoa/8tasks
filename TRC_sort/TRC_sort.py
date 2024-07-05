def TRC_sort(trc: list[int]) -> list[int]:
    """Return sorted trs list."""
    return TRC_sort_recursive(trc[:], -1, 0, len(trc) - 1)


def TRC_sort_recursive(trc: list[int], Lo: int, Mid: int, Hi: int) -> list[int]:
    """Return sorted trs list."""
    if Mid > Hi:
        return trc
    if trc[Mid] == 0:
        trc[Mid], trc[Lo + 1] = trc[Lo + 1], trc[Mid]
        Mid += 1
        Lo += 1
    elif trc[Mid] == 1:
        Mid += 1
    else:
        trc[Mid], trc[Hi] = trc[Hi], trc[Mid]
        Hi -= 1
    return TRC_sort_recursive(trc, Lo, Mid, Hi)
