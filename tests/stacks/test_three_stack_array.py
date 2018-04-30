import unittest
from stack.three_stack_array import ThreeStackArray
from stack.three_stack_array import StackFullException, \
        StackEmptyException,
        InvalidStackNumber



class TestThreeStackArray(unittest.TestCase):
    """
        Test 3 stack array
    """


    def setUp(self):
        pass

    def test_normal_push_pop(self):
        three_stack = ThreeStackArray(6)
        three_stack.push(0, 1)
        three_stack.push(1, 2)
        three_stack.push(2, 3)
        three_stack.push(0, 4)
        self.assertEqual(three_stack.pop(0), 4)
        self.assertEqual(three_stack.pop(0), 1)
        self.assertEqual(three_stack.pop(1), 2)
        self.assertEqual(three_stack.pop(2), 3)

    def test_stack_full(self):
        three_stack = ThreeStackArray(5)
        three_stack.push(2, 1)
        self.assertRaises()


