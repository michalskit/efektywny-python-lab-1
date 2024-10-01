# test_lab1_10.py
import unittest
import timeit
from lab1_10 import is_perfect, is_perfect2

class TestIsPerfectFunction(unittest.TestCase):

    def test_is_perfect_true(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))

    def test_is_perfect_false(self):
        self.assertFalse(is_perfect(7))

    def test_is_perfect2_optimization(self):
        # Mierzenie czasu wykonania funkcji is_perfect
        start_time = timeit.default_timer()
        for i in range(1, 1000):
            is_perfect(i)
        is_perfect_time = timeit.default_timer() - start_time

        # Mierzenie czasu wykonania funkcji is_perfect2
        start_time = timeit.default_timer()
        for i in range(1, 1000):
            is_perfect2(i)
        is_perfect2_time = timeit.default_timer() - start_time

        # Sprawdzanie czy is_perfect2 jest przynajmniej 5 razy szybsza od is_perfect
        self.assertTrue(is_perfect_time / is_perfect2_time >= 5)

if __name__ == "__main__":
    unittest.main()
