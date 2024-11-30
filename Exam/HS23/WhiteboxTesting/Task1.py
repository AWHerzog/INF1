def process(string, needle, mode="remove", character=None):
    if len(needle) < 1:
        raise ValueError
    if mode not in ["remove", "replace"]:
        raise NameError
    if mode == "replace" and character is None:
        raise TypeError
    if mode == "replace":
        return string.replace(needle, character)
    if mode == "remove":
        return string.replace(needle, "")

# examples of how process can be used:
print( process("abcd_abcd", "b", "remove") )       # acd_acd
print( process("abcd_abcd", "b", "replace", "*") ) # a*cd_a*cd

from unittest import TestCase

class Tests(TestCase):
    def test_input_non_string(self):
        with self.assertRaises(TypeError):
            process(2, "xyz")

    def test_needle_non_string(self):
        with self.assertRaises(TypeError):
            process("xyz", 2)

    def test_needle_empty(self):
        with self.assertRaises(ValueError):
            process("xyz", "")

    def test_mode_invalid(self):
        with self.assertRaises(NameError):
            process("abc", "xyz", "nonsense")

    def test_replace_without_replacement(self):
        with self.assertRaises(LookupError):
            process("abc", "xyz", "replace")

    def test_remove_from_empty(self):
        self.assertEqual(process("", "xy"), "")

    def test_replaces_only_first(self):
        self.assertEqual(process("here's another sentence", "e", "replace", "%"),
        "h%r%'s anoth%r s%nt%nc%")

    def test_removes_only_first(self):
        self.assertEqual(process("here's another sentence", "e"),
        "hr's anothr sntnc")

    def test_ok_with_longer_needle(self):
        self.assertEqual(process("here's another sentence", "oth"),
        "here's aner sentence")

    def test_remove_to_empty_full(self):
        self.assertEqual(process("xxx", "xxx"), "")

    def test_remove1(self):
        self.assertEqual(process("xyzzyx", "yz"), "xzyx")

    def test_remove2(self):
        self.assertEqual(process("this is a sentence is it not yes it is", "it "),
        "this is a sentence is not yes is")

    def test_replace_from_empty(self):
        self.assertEqual(process("", "xy", "replace", "zz"), "")

    def test_replace_full(self):
        self.assertEqual(process("here's another sentence", "en", "replace", "%%"),
        "here's another s%%t%%ce")