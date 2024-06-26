def all_balanced_braces(open_brace_amount: int) -> list[str]:
    """Return all balanced braces variants."""
    return all_balanced_braces_recursive(open_brace_amount, 1, "(", [])


def all_balanced_braces_recursive(
    open_brace_amount: int, n: int, variant: str, result: list[str]
) -> list[str]:
    """Return all balanced braces variants."""
    if n == open_brace_amount * 2:
        if is_balanced(variant):
            return [variant]
        return []
    return all_balanced_braces_recursive(
        open_brace_amount, n + 1, variant + "(", result
    ) + all_balanced_braces_recursive(open_brace_amount, n + 1, variant + ")", result)


def is_balanced(s: str) -> bool:
    """Return whether braces are balanced."""
    return is_balanced_recursive(s, 0, [])


def is_balanced_recursive(s: str, i: int, braces: list[str]) -> bool:
    """Return whether braces are balanced."""
    if i == len(s):
        return len(braces) == 0
    if s[i] == "(":
        braces.append(s[i])
    if s[i] == ")":
        if len(braces) == 0:
            return False
        braces.pop()
    return is_balanced_recursive(s, i + 1, braces)
