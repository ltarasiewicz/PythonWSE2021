from unittest import TestCase
from math import factorial as builtin_factorial
import factorial


class TestFactorial(TestCase):
    def test_factorial(self):
        self.assertEqual(factorial.factorial(5), builtin_factorial(5))
        self.assertEqual(factorial.factorial(12), builtin_factorial(12))
        self.assertEqual(factorial.factorial(32), builtin_factorial(32))
        self.assertEqual(factorial.factorial(7), builtin_factorial(7))
        self.assertEqual(factorial.factorial(35), builtin_factorial(35))
        self.assertEqual(factorial.factorial(0), builtin_factorial(0))

    def test_illegal_factorial(self):
        with self.assertRaises(Exception):
            factorial.factorial(-3)
