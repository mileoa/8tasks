import os.path


def get_all_files(element_path: str) -> list[str]:
    """Return all file names in given path including subfolders."""
    result: list[str] = []
    if os.path.isfile(element_path):
        result.append(os.path.split(element_path)[1])
        return result
    for i in os.listdir(element_path):
        result.extend(get_all_files(os.path.join(element_path, i)))
    return result
