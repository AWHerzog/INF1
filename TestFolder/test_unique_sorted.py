
def unique_sorted(values):
    return list(sorted(set(values), reverse=True))

from unittest import TestCase

class TestSuite(TestCase):
    
    def test_empty_list(self):
        expected = []
        result = unique_sorted([])
        self.assertEqual(result, expected)
        
    def test_no_duplicates(self):
        # Test 2: Check if duplicates are removed
        expected = [3, 2, 1]  # Expected: Unique elements sorted in descending order
        result = unique_sorted([1, 2, 3, 3, 2, 1])  # Input with duplicates
        self.assertEqual(result, expected, "The function should remove duplicates and sort in descending order.")
    
    def test_sorted_descending(self):
        # Test 3: Check if the result is sorted in descending order
        expected = [5, 4, 3, 2, 1]  # Expected: Sorted in descending order
        result = unique_sorted([1, 2, 3, 4, 5])  # Input already sorted ascending
        self.assertEqual(result, expected, "The function should return the list sorted in descending order.")
        
        
    #def test_factorial_negative(self):
        
        #with self.assertRaises(ValueError):
            #factorial(-1)


        