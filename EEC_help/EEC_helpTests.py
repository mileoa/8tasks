import unittest
import random

from EEC_help import EEC_help


class EECHelpTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(EEC_help([1, 2, 3], [1, 2, 3, 4]), False)
        self.assertEqual(EEC_help([1, 2, 3], [1, 2, 3]), True)
        self.assertEqual(EEC_help([2, 2], [1, 4]), False)
        self.assertEqual(EEC_help([2, 2], [1, 3]), False)
        self.assertEqual(EEC_help([1, 3, 2], [1, 2, 3]), True)
        self.assertEqual(EEC_help([1, 3, 2, 3], [1, 2, 2, 3]), False)
        self.assertEqual(EEC_help([1, 1], [1, 1]), True)


if __name__ == "__main__":
    unittest.main()
