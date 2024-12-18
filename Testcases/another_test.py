
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

import unittest

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test addition
        self.assertEqual(add(-1, 1), 0)  # Test addition with negative numbers
        self.assertEqual(add(0, 0), 0)  # Test addition with zeros

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Test subtraction
        self.assertEqual(subtract(0, 5), -5)  # Test subtraction resulting in negative
        self.assertEqual(subtract(5, 5), 0)  # Test subtraction resulting in zero
