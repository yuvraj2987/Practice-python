import unittest

from arrays_and_hash.sort import quick


class TestPartition(unittest.TestCase):
    """Test partition function. """

    def setUp(self):
        pass

    def test_3_element(self):
        arr = [ 4, 3, 2]
        sarr = [ 2, 3, 4]
        quick.partitioner_efficient(arr, 1)
        self.assertEqual(arr, sarr)



class TestSwapArray(unittest.TestCase):
    """Test swapping 2 indexes of the array."""

    def setUp(self):
        pass

    def test_3_element(self):
        q = [1, 2, 3]
        a = [3, 2, 1]
        quick.swap(q, 0, 2)
        self.assertEqual(q, a)
