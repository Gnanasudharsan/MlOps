import unittest
from src.calculator import fun1, fun2, fun3, fun4, safe_divide, power

class TestCalculator(unittest.TestCase):
    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)
        self.assertEqual(fun1(2.5, 0.5), 3.0)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)
        self.assertEqual(fun2(2.5, 0.5), 2.0)

    def test_fun3(self):
        self.assertEqual(fun3(2, 3), 6)
        self.assertEqual(fun3(2.5, 2), 5.0)

    def test_fun4_metrics(self):
        out = fun4(1, 2, 3)
        self.assertIsInstance(out, dict)
        self.assertEqual(out["sum"], 6)
        self.assertEqual(out["mean"], 2)
        self.assertEqual(out["min"], 1)
        self.assertEqual(out["max"], 3)
        self.assertEqual(out["range"], 2)

    def test_type_validation(self):
        for badx, bady in [("2",3), (2,"3"), (None,1), (True,2), (2,False)]:
            with self.assertRaises(ValueError): fun1(badx, bady)
            with self.assertRaises(ValueError): fun2(badx, bady)
            with self.assertRaises(ValueError): fun3(badx, bady)

    def test_safe_divide(self):
        self.assertEqual(safe_divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            safe_divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(3, 2), 9)

if __name__ == "__main__":
    unittest.main()
