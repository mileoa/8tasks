def matrix(n: int, m: int, matrix: list[list[int]]) -> list[int]:
    """Return one dimensional matrix converted from
    two dimensional matrix by spiral crawl.
    """
    return matrix_recursive(n, m, matrix, {"x": 0, "y": 0}, 0, [])


def matrix_recursive(
    n: int,
    m: int,
    matrix: list[list[int]],
    position: dict[str, int],
    circle_n: int,
    result: list[int],
):
    """Return one dimensional matrix converted from
    two dimensional matrix by spiral crawl.
    """
    if len(result) == n * m:
        return result
    result.append(matrix[position["y"]][position["x"]])
    if position["x"] + 1 >= n - circle_n and position["y"] + 1 < m - circle_n:
        position["y"] += 1
    elif position["y"] + 1 == m - circle_n and position["x"] > circle_n:
        position["x"] -= 1
    elif position["y"] - 1 > circle_n:
        position["y"] -= 1
    elif position["y"] - 1 == circle_n:
        circle_n += 1
        position["x"] += 1
    else:
        position["x"] += 1
    return matrix_recursive(n, m, matrix, position, circle_n, result)
