# test-lab1-1.py

import unittest
from lab1_1 import avg

class TestAverageFunction(unittest.TestCase):

    def test_average_of_empty_list(self):
        # Testing the behavior when the input list is empty
        # An empty list should raise a ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            avg([])

    def test_average_of_single_number(self):
        # Testing the behavior for a list with a single number
        self.assertEqual(avg([5]), 5)

    def test_average_of_multiple_numbers(self):
        # Testing the behavior for a list with multiple numbers
        self.assertEqual(avg([5, 10, 15, 20]), 12.5)

    def test_average_of_negative_numbers(self):
        # Testing the behavior for a list with negative numbers
        self.assertEqual(avg([-5, -10, -15, -20]), -12.5)

    def test_average_of_mixed_numbers(self):
        # Testing the behavior for a list with both positive and negative numbers
        self.assertEqual(avg([-5, 10, -15, 20]), 2.5)

    def test_average_of_zeroes(self):
        # Testing the behavior for a list with all zeroes
        self.assertEqual(avg([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
