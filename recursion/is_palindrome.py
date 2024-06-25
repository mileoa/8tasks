def is_palindrome(s: str) -> bool:
    """Return whether given string is palindrom."""
    return is_palindrome_recursive(s, len(s))


def is_palindrome_recursive(s: str, n: int) -> bool:
    """Return whether given string is palindrom."""
    if n == int(len(s) // 2):
        return True
    return s[len(s) - n] == s[n - 1] and is_palindrome_recursive(s, n - 1)
