import unittest
import multi.maths as m

class TestGetPowerOfTen(unittest.TestCase):
    """
        Test getPowerOfTen method
    """

    def setUp(self):
        pass

    def test_power_of_ten(self):
        self.assertEqual(m.getPowerOfTen(1), 0)
        self.assertEqual(m.getPowerOfTen(12), 1)
        self.assertEqual(m.getPowerOfTen(256), 2)
        self.assertEqual(m.getPowerOfTen(1000), 3)
