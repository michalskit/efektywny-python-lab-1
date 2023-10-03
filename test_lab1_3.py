import unittest
from lab1_3 import sum_of_squares

class TestSumOfSquares(unittest.TestCase):
    
    def test_sum_of_squares_1(self):
        result = sum_of_squares(1)
        self.assertEqual(result, 1)
        
    def test_sum_of_squares_2(self):
        result = sum_of_squares(2)
        self.assertEqual(result, 5)  # 1^2 + 2^2 = 5
        
    def test_sum_of_squares_3(self):
        result = sum_of_squares(3)
        self.assertEqual(result, 14)  # 1^2 + 2^2 + 3^2 = 14
        
    def test_sum_of_squares_4(self):
        result = sum_of_squares(4)
        self.assertEqual(result, 30)  # 1^2 + 2^2 + 3^2 + 4^2 = 30

    def test_zero_input(self):
        result = sum_of_squares(0)
        self.assertEqual(result, 0)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            sum_of_squares(2.5)

if __name__ == "__main__":
    unittest.main()
