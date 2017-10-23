import unittest
from list import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    """

    def setUp(self):
        pass

    def test_length(self):
        l1 = LinkedList()
        self.assertEqual(l1.len(), 0)
        l1.push(1)
        self.assertEqual(l1.len(), 1)
        l1.push(2)
        l1.push(3)
        self.assertEqual(l1.len(), 3)
    # end of method

# end of class


if __name__ == "__main__":
    unittest.main()