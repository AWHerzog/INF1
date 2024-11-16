def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)

from unittest import TestCase

class TestSuite(TestCase):
    def test_min(self):
        self.assertEqual(
            min_max_mean([1,2,3])[0] , 1
        )

    def test_max(self):
        self.assertEqual(
            min_max_mean([2,4,8])[1], 8
        )
    def test_mean(self):
        self.assertEqual(
            min_max_mean([1,2,3,4,5])[2], 3
        )

print(min_max_mean([1,2,3,4,5]))