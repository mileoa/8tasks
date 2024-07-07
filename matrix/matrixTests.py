import unittest

from matrix import matrix


class MatrixTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(
            matrix(
                4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
            ),
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        )
        self.assertEqual(
            matrix(3, 4, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
            [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8],
        )
        self.assertEqual(
            matrix(4, 3, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )

    def test_empty(self):
        self.assertEqual(matrix(0, 0, []), [])

    def test_border(self):
        self.assertEqual(matrix(1, 1, [[1]]), [1])
        self.assertEqual(matrix(2, 1, [[1, 2]]), [1, 2])
        self.assertEqual(matrix(1, 2, [[1], [2]]), [1, 2])


if __name__ == "__main__":
    unittest.main()
