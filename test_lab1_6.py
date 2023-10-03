import unittest
from lab1_6 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome('ala'))
        self.assertFalse(is_palindrome('ananas'))
        self.assertFalse(is_palindrome('ananasa'))
        self.assertFalse(is_palindrome('tomek'))

if __name__ == '__main__':
    unittest.main()
