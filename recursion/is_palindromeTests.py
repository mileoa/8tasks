import unittest

from is_palindrome import is_palindrome


class IsPalindromeTests(unittest.TestCase):

    def test_regression(self):

        self.assertEqual(is_palindrome("aba", 3), True)
        self.assertEqual(is_palindrome("abab", 4), False)
        self.assertEqual(is_palindrome("abba", 4), True)
        self.assertEqual(is_palindrome("cabxbac", 7), True)
        self.assertEqual(is_palindrome("cabxbсc", 7), False)

    def test_border(self):
        self.assertEqual(is_palindrome("a", 1), True)
        self.assertEqual(is_palindrome("aa", 2), True)
        self.assertEqual(is_palindrome("ab", 2), False)


if __name__ == "__main__":
    unittest.main()
