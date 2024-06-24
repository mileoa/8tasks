def is_polyndrom(s: str) -> bool:
    """Return whether given string is polyndrom."""
    if len(s) == 0:
        return True
    return s[0] == s[-1] and is_polyndrom(s[1:-1])
