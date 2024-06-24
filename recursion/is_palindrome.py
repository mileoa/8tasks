def is_palindrome(s: str) -> bool:
    """Return whether given string is polyndrom."""
    if len(s) == 0:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])
