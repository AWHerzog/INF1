from Task3Code import median
from unittest import TestCase

class MedianTests(TestCase):
    
    def test_no_input(self):
        self.assertEqual(
            median([]), None
        )
       