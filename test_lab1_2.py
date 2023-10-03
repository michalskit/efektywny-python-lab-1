# test_lab1_2.py

import unittest
from lab1_2 import even_list

class TestEvenList(unittest.TestCase):

    def test_even_list_basic(self):
        """Sprawdza podstawowe przypadki."""
        self.assertEqual(even_list(10), [2, 4, 6, 8, 10])
        self.assertEqual(even_list(1), [])

    def test_even_list_odd_number(self):
        """Sprawdza, czy funkcja poprawnie obsługuje liczby nieparzyste."""
        self.assertEqual(even_list(7), [2, 4, 6])

    def test_even_list_negative(self):
        """Sprawdza obsługę liczb ujemnych."""
        self.assertEqual(even_list(-4), [])

    def test_even_list_zero(self):
        """Sprawdza, czy funkcja poprawnie obsługuje 0."""
        self.assertEqual(even_list(0), [])

if __name__ == '__main__':
    unittest.main()
