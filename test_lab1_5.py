import unittest
from lab1_5 import primes_less_than

class TestPrimesLessThan(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(primes_less_than(5), [2,3])
        self.assertEqual(primes_less_than(10), [2,3,5,7])
        self.assertEqual(primes_less_than(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_edge_cases(self):
        self.assertEqual(primes_less_than(0), [])
        self.assertEqual(primes_less_than(1), [])
        self.assertEqual(primes_less_than(2), [])

if __name__ == "__main__":
    unittest.main()
