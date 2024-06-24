import unittest
import random

from sum_digits import sum_digits

class SumDigitsTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sum_digits(5), 5)
        self.assertEqual(sum_digits(89), 17)
        self.assertEqual(sum_digits(123), 6)

    def test_border(self):
        self.assertEqual(sum_digits(0), 0)

if __name__ == '__main__':
    unittest.main()
