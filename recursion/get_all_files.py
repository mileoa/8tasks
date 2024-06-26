import os.path


def get_all_files(folder_path: str) -> list[str]:
    """Return all file names in given path including subfolders."""
    return get_all_files_recursive([folder_path], 0, [])


def get_all_files_recursive(
    elements_to_check: list[str], i: int, result: list[str]
) -> list[str]:
    if i == len(elements_to_check):
        return result
    if os.path.isdir(elements_to_check[i]):
        elements_to_check.extend(
            [
                os.path.join(elements_to_check[i], j)
                for j in os.listdir(elements_to_check[i])
            ]
        )
    elif os.path.isfile(elements_to_check[i]):
        result.append(os.path.split(elements_to_check[i])[1])
    return get_all_files_recursive(
        elements_to_check,
        i + 1,
        result,
    )


print(get_all_files("."))
