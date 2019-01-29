import unittest
from queue.circular import CircularQueue as Queue

class TestCircularQueueSize3(unittest.TestCase):
    """
    Test Circular Queue
    """

    def setUp(self):
        self.q = Queue(3)

    def test_empty(self):
        self.assertTrue(self.q)

# end of class
