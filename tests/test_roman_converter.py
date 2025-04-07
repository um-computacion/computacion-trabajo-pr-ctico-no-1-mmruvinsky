import unittest

from roman_converter import roman_to_int

class TestRomanConverter(unittest.TestCase):

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("I"), 1)
    
    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("II"), 2)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("III"), 3)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("IV"), 4)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("V"), 5)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("VI"), 6)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("VII"), 7)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("VIII"), 8)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("IX"), 9)

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("X"), 10)

unittest.main()