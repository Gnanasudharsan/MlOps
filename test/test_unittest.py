import unittest
from math import isclose
from src.converter import convert

class TestConverter(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(isclose(convert(60, "mph", "kph"), 96.56064, rel_tol=1e-9))
        self.assertTrue(isclose(convert(1, "gal", "L"), 3.785411784, rel_tol=1e-12))
        self.assertEqual(convert(0, "C", "F"), 32.0)

    def test_invalid(self):
        with self.assertRaises(ValueError): convert(1, "m", "kg")   # cross-category
        with self.assertRaises(ValueError): convert(1, "nope", "m") # unknown unit
        with self.assertRaises(ValueError): convert("x", "m", "km") # non-numeric

if __name__ == "__main__":
    unittest.main()
