
def count_booleans(booleans):
    return booleans.count(True), booleans.count(False), len(booleans)

from unittest import TestCase

class TestSuite(TestCase):
    
    def test_trues(self):
        res = count_booleans([True, False, True])
        self.assertEqual(res[0], 2)
    
    def test_false(self):
        res = count_booleans([True, False, True])
        self.assertEqual(res[1], 1)
    
    def test_len(self):
        res = count_booleans([True, False, True])
        self.assertEqual(res[2], 3)
        