import unittest
import sys
from time import time

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_Fact0(self):
        self.assertEqual(factorial(0), 1)

    def test_Fact_pos(self):
        self.assertEqual(factorial(5), 120)

    def test_Fact1(self):
        self.assertEqual(factorial(1), 1)

    def test_Fact_neg(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_Fact_huge(self):
        with self.assertRaises(ValueError):
            factorial(10**6)

    def test_Fact_str(self):
        with self.assertRaises(TypeError):
            factorial('string')

    def test_Fact_float(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

