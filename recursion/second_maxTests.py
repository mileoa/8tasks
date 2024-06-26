import unittest
import random

from second_max import second_max


class SecondMaxTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(second_max([1, 2, 3]), 2)
        self.assertEqual(second_max([1, 3, 2]), 2)
        self.assertEqual(second_max([2, 1, 3]), 2)
        self.assertEqual(second_max([2, 1, 3]), 2)
        self.assertEqual(second_max([2, 3, 1]), 2)
        self.assertEqual(second_max([3, 1, 2]), 2)
        self.assertEqual(second_max([3, 2, 1]), 2)
        self.assertEqual(second_max([1, 3, 3]), 3)
        self.assertEqual(second_max([3, 1, 3]), 3)
        self.assertEqual(second_max([3, 3, 1]), 3)
        self.assertEqual(second_max([1, 3, 7, 1, 5, 7, 4, 5]), 7)
        self.assertEqual(second_max([1, 3, 3, 1, 5, 7, 4, 5]), 5)

    def test_border(self):
        self.assertEqual(second_max([1, 2]), 1)
        self.assertEqual(second_max([2, 1]), 1)
        self.assertEqual(second_max([2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
