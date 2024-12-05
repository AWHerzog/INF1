def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)

from unittest import TestCase

class TestSuite(TestCase):
    
    def test_min_value(self):
        min_val, max_val, mean_val = min_max_mean([1, 2, 3])
        self.assertEqual(min_val, 1)  

    def test_max_value(self):
        min_val, max_val, mean_val = min_max_mean([1, 2, 3])
        self.assertEqual(max_val, 3)  

    def test_mean_value(self):
        min_val, max_val, mean_val = min_max_mean([1, 2, 3])
        self.assertEqual(mean_val, 2) 
