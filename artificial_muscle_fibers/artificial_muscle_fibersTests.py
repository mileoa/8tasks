import unittest

from artificial_muscle_fibers import artificial_muscle_fibers


class ArtificialMusculeFibers(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 4, 5]), 0)
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1]), 2)
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]), 2)

    def test_empty(self):
        self.assertEqual(artificial_muscle_fibers([]), 0)

    def test_border(self):
        self.assertEqual(artificial_muscle_fibers([1]), 0)
        self.assertEqual(artificial_muscle_fibers([1, 1, 1, 1]), 1)
        self.assertEqual(artificial_muscle_fibers([32000, 32000, 32000]), 1)
        self.assertEqual(artificial_muscle_fibers([32000]), 0)


if __name__ == "__main__":
    unittest.main()
