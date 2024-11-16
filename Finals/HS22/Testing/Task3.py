def unique_sorted(values):
    return list(sorted(set(values), reverse=True))

from unittest import TestCase

class TestSuite(TestCase):
    def test_reverse(self):
        self.assertEqual(
            unique_sorted([1,2,3,4]), [4,3,2,1]
        )
    def test_empty_list(self):
        self.assertEqual(
            unique_sorted([]), []
        )
        
    def test_unique_values(self):
        self.assertEqual(
            unique_sorted([4,3,2,2,1]), [4,3,2,1]
        )


print(unique_sorted([1,2,3,4,4,1]))
print(unique_sorted([]))
print(unique_sorted(["a","v","a","b"]))
print(unique_sorted(["a","v","a","b"]))