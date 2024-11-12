from unittest import TestCase
from Task1Code import sorted_arrays_overlap

class SortedArraysOverlapTest(TestCase):
    
    def naming(self):
        s = sorted_arrays_overlap
    
    
    def test_invalid_input(self):
        self.assertEqual(
            sorted_arrays_overlap("not a list", [1,2,3]),
            "Invalid input types! Both parameters should be arrays."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,3], 123),
            "Invalid input types! Both parameters should be arrays."
        )
        self.assertEqual(
            sorted_arrays_overlap(None, [1,2,3]),
            "Invalid input types! Both parameters should be arrays."
        )

    def test_empty_array(self):
        self.assertEqual(
            sorted_arrays_overlap([],[]),
            "Empty arrays! Neither of the arrays can be empty."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,3],[]),
            "Empty arrays! Neither of the arrays can be empty."
        )
        self.assertEqual(
            sorted_arrays_overlap([],[1,2,3]),
            "Empty arrays! Neither of the arrays can be empty."
        )
    def test_data_types(self):
        self.assertEqual(
            sorted_arrays_overlap([1,2, "Three"], [1,2,3,4]),
            "Invalid data types within arrays! Arrays should contain only integers."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,3], [1,True,3]),
            "Invalid data types within arrays! Arrays should contain only integers."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,3.0], [1,2,3,4]),
            "Invalid data types within arrays! Arrays should contain only integers."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,3.0], [1,[1,2,3],3,4]),
            "Invalid data types within arrays! Arrays should contain only integers."
        )
    def test_sorting(self):
        self.assertEqual(
            sorted_arrays_overlap([1,2,3], [3,2,1]),
            "Not sorted arrays! Both arrays should be sorted in ascending order."
        )
        self.assertEqual(
            sorted_arrays_overlap([2,3,1], [3,4,2,1]),
            "Not sorted arrays! Both arrays should be sorted in ascending order."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,2,4,3], [1,2,3]),
            "Not sorted arrays! Both arrays should be sorted in ascending order."
        )
        self.assertTrue(
            sorted_arrays_overlap([1,2,3],[1,2,3])
        )
    def test_overlapping_elements(self):
        self.assertEqual(
            sorted_arrays_overlap([1,2,3], [4,5,6,7,]),
            "There are no overlapping elements in given arrays."
        )
        self.assertEqual(
            sorted_arrays_overlap([1,1,1], [1,1,1]),
            [1,1,1]
        )

    def test_list_containing_valid_elements(self):
        array_1 = [-5, -3, -1, 7, 8, 14, 19]
        array_2 = [-8, -5, -2, -1, 19]
        expected_result = [-5, -1, 19]
        self.assertEqual(
        sorted_arrays_overlap(array_1, array_2),
        expected_result
        )
        
        array_1 = [5, 8, 14, 19, 19, 19, 23, 34, 52]
        array_2 = [2, 5, 7, 8, 15, 19, 19, 25, 34, 62]
        expected_result = [5, 8, 19, 19, 34]
        self.assertEqual(
            sorted_arrays_overlap(array_1, array_2),
            expected_result
        )









    
    
    
        

