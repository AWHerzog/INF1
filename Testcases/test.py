
def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)

from unittest import TestCase

class TestSuite(TestCase):
    
    def test_min_value(self):
        result = min_max_mean([1, 2, 3, 4, 5])
        self.assertEqual(result[0], 1)

    def test_max_value(self):
        result = min_max_mean([1, 2, 3, 4, 5])
        self.assertEqual(result[1], 5)

    def test_mean_value(self):
        result = min_max_mean([1, 2, 3, 4, 5])
        self.assertEqual(result[2], 3.0) 
        

    #with self.assertRaises(AssertionError):
            #words_by_len(123)

        