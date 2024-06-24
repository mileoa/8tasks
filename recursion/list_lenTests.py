import unittest
import random

from list_len import list_len


class ListLenTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(list_len([1, 2, 3, 4]), 4)
        self.assertEqual(list_len([1, 2]), 2)

    def test_empty(self):
        self.assertEqual(list_len([]), 0)

    def test_random(self):
        for i in range(10000):
            l: list[int] = list(range(random.randint(0, 900)))
            len_l: int = len(l)
            self.assertEqual(list_len(l), len_l)

    def test_border(self):
        self.assertEqual(list_len(["a"]), 1)


if __name__ == "__main__":
    unittest.main()
