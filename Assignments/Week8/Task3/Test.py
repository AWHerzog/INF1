from Task3Code import median
from unittest import TestCase

class MedianTests(TestCase):
    
    def test_no_input(self):
        self.assertEqual(
            median([]), None
        )

    def test_uneven_length_lists(self):
        self.assertEqual(
            median([2,3,4]), 3
        )
    def test_even_length_lists(self):      
        self.assertEqual(
            median([2,3,4,5]), 3.5
        )
    def test_single_number(self):
        self.assertEqual(
            median([5]), 5
        )
    def test_two_numbers(self):
        self.assertEqual(
            median([2,3]), 2.5
        )
    def test_floating_point_numbers(self):
        self.assertEqual(
            median([1.0, 3.0, 4.0]), 3.0
        )
    def test_floating_point_number_even_length_list(self):
        self.assertEqual(
            median([1.0, 3.0, 5.0, 7.0]), 4.0 
        )
    def test_negative_numbers(self):
        self.assertEqual(
            median([-1, -3, -5]), -3
        )
        self.assertEqual(
            median([-1.0, -3.0, -5.0]), -3.0
        )
    def test_unordered_lists(self):
        self.assertEqual(
            median([1,5,3,2]), 2.5
        )
    def test_mixed_list(self):
        self.assertEqual(
            median([-3, -4, 1, 5]), -1
        )
    def test_duplicate_values(self):
        self.assertEqual(
            median([1,1,3,3,4,5,6]), 3
        )
    def test_duplicate_floating_point_values(self):
        self.assertEqual(
            median([1.5, 1.5, 3.0, 3.0, 4.0]), 3.0
        )
