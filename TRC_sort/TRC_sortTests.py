import unittest
import random

from TRC_sort import TRC_sort


class TRCSortTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TRC_sort([2, 1, 0]), [0, 1, 2])
        self.assertEqual(TRC_sort([0, 1, 2, 1, 0, 2]), [0, 0, 1, 1, 2, 2])

    def test_empty(self):
        self.assertEqual(TRC_sort([]), [])

    def test_random(self):
        for i in range(10000):
            l: list[int] = []

            for i in range(800):
                l.append(random.randint(0, 2))

            l_sorted: list[int] = l[:]
            l_sorted.sort()

            self.assertEqual(TRC_sort(l), l_sorted)

    def test_border(self):
        self.assertEqual(TRC_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
