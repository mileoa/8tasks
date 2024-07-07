def army_communication_matrix(n: int, matrix: list[list[int]]) -> str:
    """Return parameters of submatrix with max sum of elements.

    Submatrix must be M size 2 <= M <= n - 1
    Returning string contain coordinates of submatrix and size M.
    """
    return army_communication_matrix_recursive(
        n, matrix, {"x": n - 1, "y": n - 1}, 0, {}, [-1, -1, -1, -1]
    )


def army_communication_matrix_recursive(
    n: int,
    matrix: list[list[int]],
    position: dict[str, int],
    depth: int,
    sums: dict[int, int],
    result: list[int],
) -> str:
    if position["y"] < 0:
        return str(result[0]) + " " + str(result[1]) + " " + str(result[2])

    if depth + position["x"] >= n or depth + position["y"] >= n or depth >= n - 1:
        depth = 0
        if position["x"] - 1 == -1:
            position["x"] = n - 1
            position["y"] -= 1
        else:
            position["x"] -= 1
    else:
        if depth == 0:
            sums[(position["x"], position["y"], depth)] = matrix[position["y"]][
                position["x"]
            ]
        else:
            sums[(position["x"], position["y"], depth)] = (
                sums[(position["x"], position["y"], depth - 1)]
                + matrix[position["y"] + depth][position["x"]]
                + matrix[position["y"]][position["x"] + depth]
            )

            if (position["x"] + 1, position["y"] + 1, depth - 1) in sums:
                sums[(position["x"], position["y"], depth)] += sums[
                    (position["x"] + 1, position["y"] + 1, depth - 1)
                ]

        if sums[(position["x"], position["y"], depth)] >= result[3]:
            result[0] = position["x"]
            result[1] = position["y"]
            result[2] = depth + 1
            result[3] = sums[(position["x"], position["y"], depth)]

        depth += 1

    return army_communication_matrix_recursive(n, matrix, position, depth, sums, result)
