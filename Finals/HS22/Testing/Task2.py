def count_booleans(booleans):
    return booleans.count(True), booleans.count(False), len(booleans)

from unittest import TestCase

class TestSuite(TestCase):
    def test_true(self):
        self.assertEqual(
            count_booleans([True,True,False,True])[0], 3
        )
    def test_False(self):
        self.assertEqual(
            count_booleans([True,True,False,True])[1], 1
        )
    def test_len(self):
        self.assertEqual(
            count_booleans([True,True,False,True])[2], 4
        )


print(count_booleans([True,True,False,True]))