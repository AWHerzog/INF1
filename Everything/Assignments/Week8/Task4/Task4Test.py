from Task4Script import move
from unittest import TestCase


class MoveTestSuite(TestCase):


    def test_move_left(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "left")
        expected = (
            (
                "#####   ",
                "###    #",
                "#  o  ##",
                "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_down(self):
        state = (
            "#####   ",
            "###  o #",
            "#      #",
            "   #####"
        )
        actual = move(state, "down")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o #",
                "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_into_boundary(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_invalid_game_state(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   ###"  
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_no_possible_moves(self):
        state = (
            "#######",
            "###o###",
            "#######"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_empty_move_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "")

    def test_invalid_character_in_game_world(self):
        state = (
            "#####   ",
            "###    #",
            "#   o@##",  
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_empty_world(self):
        state = ()  
        with self.assertRaises(Warning):
            move(state, "up")

    def test_single_row_world(self):
        state = ("#o#   #",)  
        with self.assertRaises(Warning):
            move(state, "right")

    def test_single_column_world(self):
        state = ("#", "o", "#", " ")  
        with self.assertRaises(Warning):
            move(state, "down")

    def test_world_with_no_free_spaces(self):
        state = (
            "#####",
            "#####",
            "##o##",
            "#####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_world_with_only_free_spaces(self):
        state = (
            "     ",
            "     ",
            "  o  ",
            "     "
        )
        actual = move(state, "left")
        expected = (
            (
                "     ",
                "     ",
                " o   ",
                "     "
            ),
            ("down", "left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_player_on_edge_of_world(self):
        state = (
            "o    ",
            "     ",
            "     "
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_multiple_players(self):
        state = (
            "o    ",
            "    o",
            "     "
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_large_world(self):
        state = tuple(" " * 1000 for _ in range(1000))
        state = tuple(row if i != 500 else row[:500] + "o" + row[501:] for i, row in enumerate(state))
        actual = move(state, "left")
       

    def test_non_string_elements_in_state(self):
        state = (["#####", "###  #", "#   o##", "   #####"],) 
        with self.assertRaises(Warning):
            move(state, "up")

    def test_case_sensitivity(self):
        state = (
            "#####",
            "###  #",
            "#   O##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_whitespace_only_rows(self):
        state = (
            "     ",
            "     ",
            "  o  ",
            "     ",
            "     "
        )
        actual = move(state, "up")
        expected = (
            (
                "     ",
                "  o  ",
                "     ",
                "     ",
                "     "
            ),
            ("down", "left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_direction_as_non_string(self):
        state = (
            "#####",
            "###  #",
            "#   o##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, 123)  

    def test_empty_string_as_game_state_rows(self):
        state = ("", "", "o", "", "")  
        with self.assertRaises(Warning):
            move(state, "up")

    def test_mixed_valid_and_invalid_characters(self):
        state = (
            "#####",
            "###@ #",
            "#   o##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_with_unicode_characters(self):
        state = (
            "#####",
            "###  #",
            "#  öo##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    



