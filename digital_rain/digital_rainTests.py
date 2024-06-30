import unittest
import random

from digital_rain import digital_rain


class DigitalRainTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(digital_rain("1111000"), "111000")
        self.assertEqual(digital_rain("11101000"), "11101000")
        self.assertEqual(digital_rain("011111110"), "10")
        self.assertEqual(digital_rain("111111111"), "")
        self.assertEqual(digital_rain("000000000"), "")

    def test_empty(self):
        self.assertEqual(digital_rain(""), "")

    def test_border(self):
        self.assertEqual(digital_rain("1"), "")
        self.assertEqual(digital_rain("0"), "")
        self.assertEqual(digital_rain("10"), "10")


if __name__ == "__main__":
    unittest.main()
