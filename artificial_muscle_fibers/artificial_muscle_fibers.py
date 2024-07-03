def artificial_muscle_fibers(arr: list[int]) -> int:
    """Return amount of digits repeated >= 2 times."""
    return artificial_muscle_fibers_recursion(arr, 0, [bytes(1) for i in range(8192)])


def artificial_muscle_fibers_recursion(
    arr: list[int], i: int, buffer: list[bytes]
) -> int:
    """Return amount of digits repeated >= 2 times."""
    if i == len(arr):
        return 0

    # First occurance.
    if buffer[arr[i] // 8][0] & (1 << (8 - 1 - (arr[i] - (arr[i] // 8) * 8))) == 0:
        buffer[arr[i] // 8] = bytes(
            [buffer[arr[i] // 8][0] | (1 << (8 - 1 - (arr[i] - (arr[i] // 8) * 8)))]
        )
        return artificial_muscle_fibers_recursion(arr, i + 1, buffer)

    # Second occurance.
    if (
        buffer[arr[i] // 8 + 4000][0] & (1 << (8 - 1 - (arr[i] - (arr[i] // 8) * 8)))
        == 0
    ):
        buffer[arr[i] // 8 + 4000] = bytes(
            [
                buffer[arr[i] // 8 + 4000][0]
                | (1 << (8 - 1 - (arr[i] - (arr[i] // 8) * 8)))
            ]
        )
        return 1 + artificial_muscle_fibers_recursion(arr, i + 1, buffer)

    # Other occurance.
    return artificial_muscle_fibers_recursion(arr, i + 1, buffer)
