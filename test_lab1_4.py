import unittest
from lab1_4 import sum_of_multiples

class TestSumOfMultiples(unittest.TestCase):

    def test_basic_multiples(self):
        # Testowanie podstawowych wartości
        self.assertEqual(sum_of_multiples(1), 5050)  # 1+2+...+100 = 5050
        self.assertEqual(sum_of_multiples(2), 2550)  # 2+4+...+100 = 2550
        self.assertEqual(sum_of_multiples(3), 1683)  # 3+6+...+99 = 1683
        self.assertEqual(sum_of_multiples(4), 1300)  # 4+8+...+100 = 1300
        self.assertEqual(sum_of_multiples(5), 1050)  # 5+10+...+100 = 1050

    def test_custom_n(self):
        # Testowanie niestandardowej wartości dla n
        self.assertEqual(sum_of_multiples(1, 11), 55)  # 1+2+...+10 = 55
        self.assertEqual(sum_of_multiples(3, 10), 18)  # 3+6+9 = 18
        self.assertEqual(sum_of_multiples(5, 22), 50)  # 5+10+15+20 = 50

    def test_edge_cases(self):
        # Testowanie przypadków skrajnych
        self.assertEqual(sum_of_multiples(100), 100)  # Tylko 100
        self.assertEqual(sum_of_multiples(101), 0)    # Brak wielokrotności
        self.assertEqual(sum_of_multiples(1000), 0)   # Brak wielokrotności

if __name__ == "__main__":
    unittest.main()
