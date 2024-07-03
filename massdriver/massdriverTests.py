import unittest

from massdriver import massdriver


class MassdriverTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(massdriver([1, 2, 3, 1, 2, 3, 4]), 0)
        self.assertEqual(massdriver([1, 2, 3, 4, 3, 4, 2]), 1)
        self.assertEqual(massdriver([1, 2, 3, 4, 5, 6, 7]), -1)

    def test_empty(self):
        self.assertEqual(massdriver([]), -1)

    def test_border(self):
        self.assertEqual(massdriver([1, 1]), 0)
        self.assertEqual(massdriver([1]), -1)


if __name__ == "__main__":
    unittest.main()
