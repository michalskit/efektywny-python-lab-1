# test-lab1-1.py

import unittest
from lab1_1 import avg

class TestAverageFunction(unittest.TestCase):

    def test_average_of_single_number(self):
        # Testing the behavior for a list with a single number
        self.assertAlmostEqual(avg([5]), 5, places=7)

    def test_average_of_multiple_numbers(self):
        # Testing the behavior for a list with multiple numbers
        self.assertAlmostEqual(avg([5, 10, 15, 20]), 12.5, places=7)

    def test_average_of_negative_numbers(self):
        # Testing the behavior for a list with negative numbers
        self.assertAlmostEqual(avg([-5, -10, -15, -20]), -12.5, places=7)

    def test_average_of_mixed_numbers(self):
        # Testing the behavior for a list with both positive and negative numbers
        self.assertAlmostEqual(avg([-5, 10, -15, 20]), 2.5, places=7)

    def test_average_of_zeroes(self):
        # Testing the behavior for a list with all zeroes
        self.assertAlmostEqual(avg([0, 0, 0, 0]), 0, places=7)

if __name__ == '__main__':
    unittest.main()
