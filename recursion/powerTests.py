import unittest
import random

from power import power


class powerTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(power(2, 6), 64)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(123, 1), 123)
        self.assertEqual(power(123, 0), 1)
        self.assertEqual(power(2, -1), 1 / 2)
        self.assertEqual(power(3, -2), 1 / 9)

    def test_border(self):
        self.assertEqual(power(123456789, 1), 123456789)
        self.assertEqual(power(1234567, 2), 1524155677489)
        self.assertEqual(power(1, 900), 1)


if __name__ == "__main__":
    unittest.main()
