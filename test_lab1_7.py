import unittest
from lab1_7 import how_many_different_letters

class TestHowManyDifferentLetters(unittest.TestCase):
    
    def test_different_letters(self):
        self.assertEqual(how_many_different_letters('tomek'), 5)
        self.assertEqual(how_many_different_letters('ala'), 2)
        self.assertEqual(how_many_different_letters('ananas'), 3)
        self.assertEqual(how_many_different_letters('jola'), 4)

if __name__ == '__main__':
    unittest.main()
