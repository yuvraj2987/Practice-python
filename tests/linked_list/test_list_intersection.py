import unittest
from linked_list.list import LinkedList
from linked_list.operations import intersection


class TestListIntersection(unittest.TestCase):
    """
        Test Intersection of 2 lists
    """
    def setUp(self):
        pass

    def test_list_intersection(self):
        l1 = LinkedList()
        l1.push_at_head("c")
        l1.push_at_head("b")
        b_node_ref = l1.head
        l2 = LinkedList()
        l2.head = b_node_ref
        l1.push_at_head("a")

