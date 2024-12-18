import unittest

def dict_to_lists(d):
    pass

class MyTestSuite(unittest.TestCase):
    
    def test_correct_output(self):
        self.assertEqual(
            dict_to_lists({"b": 1, "a": 2}), (["a", "b"], [2, 1])
        )
        self.assertEqual(
            dict_to_lists({"a": 20, "z": 1}), (["a", "z"], [20, 1])
        )
    
    def test_input_dictionary(self):
        with self.assertRaises(TypeError):
            dict_to_lists(("av, c"))
        
        with self.assertRaises(TypeError):
            dict_to_lists(["asv"])
    def test_empty_input(self):
        self.assertEqual(
            dict_to_lists({}), ([], [])
        )
    def test_single_key(self):
        self.assertEqual(
            dict_to_lists({"a": 1}), (["a"], [1])
        )
    def test_single_non_string_key(self):
        self.assertEqual(dict_to_lists({1: "value"}), ([1], ["value"]))
    
    def test_single_non_string_key(self):
        self.assertEqual(dict_to_lists({1: "value"}), ([1], ["value"]))


    