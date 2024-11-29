from unittest import TestCase
from Task3 import evolve


class EvolveTestSuite(TestCase):

    def test_validate_world():
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