import unittest
from lab1_9 import phi_euler

class TestPhiEulerFunction(unittest.TestCase):

    def test_phi_euler_with_input_6(self):
        self.assertEqual(phi_euler(6), 2)

    def test_phi_euler_with_input_64(self):
        self.assertEqual(phi_euler(64), 32)

    def test_phi_euler_with_input_97(self):
        self.assertEqual(phi_euler(97), 96)

if __name__ == "__main__":
    unittest.main()
