import unittest
from queue.circular import CircularQueue as Queue

class TestCircularQueue(unittest.TestCase):
    """
    Test Circular Queue
    """

    def setUp(self):
        pass

    def test_empty_init(self):
        q = Queue(1)
        self.assertTrue(q.isEmpty())

    def test_empty_false_after_enQueue(self):
        q = Queue(1)
        q.enQueue(1)
        self.assertFalse(q.isEmpty())

    def test_empty_after_deQueue(self):
        q = Queue(2)
        q.enQueue(1)
        q.enQueue(2)
        q.deQueue()
        q.deQueue()
        self.assertTrue(q.isEmpty())

    def test_enQueue_more_than_size(self):
        q = Queue(3)
        self.assertTrue(q.enQueue(1))
        self.assertTrue(q.enQueue(2))
        self.assertTrue(q.enQueue(3))
        self.assertFalse(q.enQueue(4))

    def test_queue_full_false_at_start(self):
        q = Queue(1)
        self.assertFalse(q.isFull())

    def test_queue_full_true(self):
        q = Queue(2)
        q.enQueue(1)
        q.enQueue(2)
        self.assertTrue(q.isFull())

    def test_queue_full_enqueue_dequeue(self):
        q = Queue(2)
        q.enQueue(1)
        q.enQueue(2)
        self.assertTrue(q.isFull())
        q.deQueue()
        self.assertFalse(q.isFull())
# end of class


if __name__ == "__main__":
    unittest.main()
