import unittest
from unique_char_string import is_unique


class UniqueChar(unittest.TestCase):
    """
        Test UniqueChar
    """
    def setUp(self):
        pass

    def test_is_unique(self):
        """
            Test cases for is_unique method
        """
        # 1. Test emtpy string
        self.assertFalse(is_unique(""))
        # 2. Test single letter
        self.assertTrue(is_unique("a"))
        # 3. Test unique letter
        self.assertTrue(is_unique("abcd"))
        # 4. Test no unique letter
        self.assertFalse(is_unique("abca"))
    # end of def
# end of class


if __name__ == '__main__':
    unittest.main()
