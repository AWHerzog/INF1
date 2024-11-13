from Task2Code import sort
from unittest import TestCase

class SortTests(TestCase):
    
    def test_parameter(self):
        self.assertEqual(
        sort(None), None
    )
        self.assertEqual(
        sort((123)), None
    )
        self.assertEqual(
        sort((1.23)), None
    )
        self.assertEqual(
        sort((abs)), None
    )
        self.assertEqual(
        sort((True)), None
    )
    def test_comparable_elements_lists(self):
        self.assertEqual(sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort([1.5, 0.5, 2.5]), [0.5, 1.5, 2.5])  
        self.assertEqual(sort(["b", "a", "c"]), ["a", "b", "c"]) 
        self.assertEqual(sort([]), [])  
    def test_comparable_elements_tuple(self):
    
        self.assertEqual(sort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(sort((1.5, 0.5, 2.5)), [0.5, 1.5, 2.5]) 
        self.assertEqual(sort(("b", "a", "c")), ["a", "b", "c"])
        self.assertEqual(sort(()), [])  
    def test_comparable_elements_set(self):
        self.assertEqual(sort({3, 1, 2}), [1, 2, 3])
        self.assertEqual(sort({1.5, 0.5, 2.5}), [0.5, 1.5, 2.5])  
        self.assertEqual(sort({"b", "a", "c"}), ["a", "b", "c"])  

        self.assertEqual(sort(set()), [])  
    def test_comparable_elements_string(self):
        self.assertEqual(sort("12A"), ['1', '2', 'A'])
        self.assertEqual(sort(""), [])  
    def test_sort_without_changing(self):
        original_list = [5, 3, 2]
        sorted_list = sort(original_list)
        self.assertEqual(sorted_list, [2, 3, 5])  
        self.assertEqual(original_list, [5, 3, 2])  

        original_tuple = (5, 3, 2)
        sorted_tuple = sort(original_tuple)
        self.assertEqual(sorted_tuple, [2, 3, 5])  
        self.assertEqual(original_tuple, (5, 3, 2))  

        original_set = {5, 3, 2}
        sorted_set = sort(original_set)
        self.assertEqual(sorted_set, [2, 3, 5]) 
        self.assertEqual(original_set, {5, 3, 2}) 

        original_string = "532"
        sorted_string = sort(original_string)
        self.assertEqual(sorted_string, ['2', '3', '5']) 
        self.assertEqual(original_string, "532")  

        

        