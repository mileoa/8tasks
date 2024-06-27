def white_walkers(village: str) -> bool:
    """Return whether there are enemies."""
    return white_walkers_recursive(village, 0, 0, -1, False)


def white_walkers_recursive(
    village: str, i: int, enemy_count: int, previous: int, was_valid_pair: bool
) -> bool:
    """Return whether there are enemies."""
    # if enemy_count == 3 and began:
    #    return True
    if i == len(village):
        return was_valid_pair
    if ord(village[i]) >= 48 and ord(village[i]) <= 57:
        if previous + int(village[i]) != 10:
            previous = int(village[i])
        elif enemy_count != 3:
            return False
        else:
            previous = int(village[i])
            enemy_count = 0
            was_valid_pair = True

    if village[i] == "=" and previous != -1:
        enemy_count += 1
    return white_walkers_recursive(
        village, i + 1, enemy_count, previous, was_valid_pair
    )
