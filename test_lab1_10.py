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
        iterations = 10000
        
        # Mierzenie czasu wykonania funkcji is_perfect
        is_perfect_time = timeit.timeit(lambda: [is_perfect(i) for i in range(1, iterations)], number=1)

        # Mierzenie czasu wykonania funkcji is_perfect2
        is_perfect2_time = timeit.timeit(lambda: [is_perfect2(i) for i in range(1, iterations)], number=1)

        # Sprawdzanie czy is_perfect2 jest przynajmniej 2 razy szybsza od is_perfect
        print(f'Czas wykonania is_perfect: {is_perfect_time} sekundy')
        print(f'Czas wykonania is_perfect2: {is_perfect2_time} sekundy')
        speedup = is_perfect_time / is_perfect2_time
        print(f'Przyspieszenie: {speedup:.2f}x')
        self.assertTrue(speedup >= 2, f"is_perfect2 powinno być co najmniej 2 razy szybsze, ale jest tylko {speedup:.2f}x szybsze")

if __name__ == "__main__":
    unittest.main()
