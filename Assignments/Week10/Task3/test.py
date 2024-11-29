from unittest import TestCase
from script import evolve
import unittest



class TestGameOfLife(TestCase):

    def setUp(self):
        # Common game worlds used for testing
        self.valid_world = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        
        self.inconsistent_world = (
            "--------------",
            "|   ###      |",
            "|   #        |",
            "|    #",
            "--------------"
        )
        
        self.invalid_char_world = (
            "--------------",
            "|   ###      |",
            "|   $        |",  # Invalid character
            "|    #       |",
            "--------------"
        )
        
        self.non_string_row_world = (
            "--------------",
            "|   ###      |",
            123,  # Invalid row (not a string)
            "|    #       |",
            "--------------"
        )
        
        self.small_world = (
            "---",
            "|#|",
            "---"
        )
        
    def test_valid_world(self):
        try:
            result, alive_cells = evolve(self.valid_world, 4)
            self.assertIsInstance(result, tuple, "Valid world should return a tuple.")
            self.assertGreaterEqual(alive_cells, 0, "Alive cell count should be non-negative.")
        except Warning as e:
            self.fail(f"Valid world test raised a warning unexpectedly: {e}")

    def test_inconsistent_row_length(self):
        with self.assertRaises(Warning) as context:
            evolve(self.inconsistent_world, 1)
        self.assertIn("inconsistent length", str(context.exception).lower())

    def test_invalid_character(self):
        with self.assertRaises(Warning) as context:
            evolve(self.invalid_char_world, 1)
        self.assertIn("invalid character", str(context.exception).lower())

    def test_non_string_row(self):
        with self.assertRaises(Warning) as context:
            evolve(self.non_string_row_world, 1)
        self.assertIn("not a string", str(context.exception).lower())

    def test_steps_must_be_positive_integer(self):
        with self.assertRaises(Warning):
            evolve(self.valid_world, -1)  # Negative steps
        with self.assertRaises(Warning):
            evolve(self.valid_world, 0)  # Zero steps
        with self.assertRaises(Warning):
            evolve(self.valid_world, "two")  # Non-integer steps

    def test_small_world(self):
        try:
            result, alive_cells = evolve(self.small_world, 1)
            self.assertIsInstance(result, tuple, "Small world should return a tuple.")
            self.assertGreaterEqual(alive_cells, 0, "Alive cell count should be non-negative.")
        except Warning as e:
            self.fail(f"Small world test raised a warning unexpectedly: {e}")

    def test_stable_pattern(self):
        # Testing a stable block pattern
        stable_world = (
            "------",
            "|    |",
            "| ## |",
            "| ## |",
            "|    |",
            "------"
        )
        result, alive_cells = evolve(stable_world, 3)
        expected_result = (
            "------",
            "|    |",
            "| ## |",
            "| ## |",
            "|    |",
            "------"
        )
        self.assertEqual(result, expected_result, "Stable pattern should remain unchanged.")
        self.assertEqual(alive_cells, 4, "Stable block should have 4 alive cells.")

    '''
    def test_oscillator_pattern(self):
        # Testing an oscillator (blinker) pattern
        blinker_world = (
            "------",
            "|    |",
            "| ###|",
            "|    |",
            "|    |",
            "------"
        )
        result, alive_cells = evolve(blinker_world, 1)
        expected_result = (
            "------",
            "|    |",
            "|  # |",
            "|  # |",
            "|  # |",
            "------"
        )
        self.assertEqual(result, expected_result, "Blinker should oscillate to vertical.")
        self.assertEqual(alive_cells, 3, "Blinker should always have 3 alive cells.")
    '''

    def test_empty_world(self):
        # Testing a completely empty world
        empty_world = (
            "--------------",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "--------------"
        )
        result, alive_cells = evolve(empty_world, 5)
        expected_result = empty_world  # It should stay empty
        self.assertEqual(result, expected_result, "Empty world should remain unchanged.")
        self.assertEqual(alive_cells, 0, "Empty world should have 0 alive cells.")


if __name__ == '__main__':
    unittest.main()

    try:
        valid_world = (
            "--------------",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "--------------"
        )
        evolve(valid_world, 1)
        print("Valid world test passed.")
    except Warning as w:
        print(f"Valid world test failed: {w}")

    try:
        inconsistent_world = (
            "--------------",
            "|   ###      |",
            "|   #        |",
            "|    #",
            "--------------"
        )
        evolve(inconsistent_world, 1)
        print("Inconsistent row length test failed.")
    except Warning as w:
        print(f"Inconsistent row length test passed: {w}")

    try:
        invalid_char_world = (
            "--------------",
            "|   ###      |",
            "|   $        |",  # Invalid character: $
            "|    #       |",
            "--------------"
        )
        evolve(invalid_char_world, 1)
        print("Invalid character test failed.")
    except Warning as w:
        print(f"Invalid character test passed: {w}")

    try:
        non_string_world = (
            "--------------",
            "|   ###      |",
            123,  # Invalid row (not a string)
            "|    #       |",
            "--------------"
        )
        evolve(non_string_world, 1)
        print("Non-string row test failed.")
    except Warning as w:
        print(f"Non-string row test passed: {w}")