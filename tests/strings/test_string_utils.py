import unittest
from arrays_and_hash.string_utils import is_unique
from arrays_and_hash.string_utils import get_compressed_string as gcs
from arrays_and_hash.string_utils import checkAnagrams


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


class CompressedStrings(unittest.TestCase):

    def setUp(self):
        pass

    def test_none_str(self):
        s = None
        self.assertIsNone(gcs(s))

    def test_single_char_str(self):
        s = "a"
        self.assertEqual(gcs(s), s)

    def test_non_compressed_str(self):
        s = "aaabbc"
        self.assertEqual(gcs(s), s)

    def test_non_comressed_str(self):
        s = "abcdab"
        self.assertEqual(gcs(s), s)

    def test_non_compressed_both_char_type_str(self):
        s = "AaBbcC"
        self.assertEqual(gcs(s), s)

    def test_compressed_str(self):
        s = "aaabcccccaaa"
        self.assertEqual(gcs(s), "a3b1c5a3")

# end of class


class CheckAnagrams(unittest.TestCase):

    def setUp(self):
        pass

    def test_None_words(self):
        self.assertFalse(None, "abc")
        self.assertFalse(None, None)


    def test_unequal_length(self):
        s1 = "abc"
        s2= "abca"
        self.assertFalse(s1, s2)

    def test_positive_case(self):
        s1 = "abcd"
        s2 = "dabc"
        self.assertTrue(s1, s2)
        s1 = "door"
        s2 = "odor"
        self.assertTrue(s1, s2)

    def test_equal_lenth_negative_case(self):
        s1 = "abcd"
        s2 = "abce"
        self.assertFalse(w1, w2)



if __name__ == '__main__':
    unittest.main()
