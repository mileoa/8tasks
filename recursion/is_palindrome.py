def is_palindrome(s: str, n: int) -> bool:
    """Return whether given string is polyndrom."""
    if n == int(len(s) // 2):
        return True
    return s[len(s) - n] == s[n - 1] and is_palindrome(s, n - 1)
