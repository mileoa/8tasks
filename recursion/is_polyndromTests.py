import unittest

from is_polyndrom import is_polyndrom


class IsPolyndromTests(unittest.TestCase):

    def test_regression(self):

        self.assertEqual(is_polyndrom("aba"), True)
        self.assertEqual(is_polyndrom("abab"), False)
        self.assertEqual(is_polyndrom("abba"), True)
        self.assertEqual(is_polyndrom("cabxbac"), True)
        self.assertEqual(is_polyndrom("cabxbсc"), False)

    def test_border(self):
        self.assertEqual(is_polyndrom("a"), True)
        self.assertEqual(is_polyndrom("aa"), True)
        self.assertEqual(is_polyndrom("ab"), False)


if __name__ == "__main__":
    unittest.main()
