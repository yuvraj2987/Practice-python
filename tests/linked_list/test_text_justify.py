import unittest
from linked_list import text_justify as TJ

class TestTextJustify(unittest.TestCase):
    """
        Test text justify
    """
    def setUp(self):
        pass

    def test_base_case(self):
        """
        """
        input1 = ["This", "is", "great."]
        fixedLen = 7
        expected1 = ["This is", "great. "]
        output1 = TJ.fullJustify(input1, fixedLen)
        self.assertEqual(len(expected1), len(output1))
        for i in range(0, len(expected1)):
            self.assertEqual(expected1[i], output1[i])
        # end of for
