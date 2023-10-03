import unittest
from lab1_8 import zaprzyjaznione

class TestZaprzyjaznioneFunction(unittest.TestCase):

    def test_zaprzyjaznione_1(self):
        self.assertEqual(zaprzyjaznione(1), [])

    def test_zaprzyjaznione_300(self):
        self.assertEqual(zaprzyjaznione(300), [(220, 284)])

    def test_zaprzyjaznione_2000(self):
        self.assertEqual(zaprzyjaznione(2000), [(220, 284), (1184, 1210)])

    def test_zaprzyjaznione_13000(self):
        expected_output = [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856)]
        self.assertEqual(zaprzyjaznione(13000), expected_output)

if __name__ == '__main__':
    unittest.main()
