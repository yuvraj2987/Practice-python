import unittest
from arrays_and_hash.string_utils import is_unique
from arrays_and_hash.string_utils import get_compressed_string as gcs
from arrays_and_hash.string_utils import checkAnagrams
from arrays_and_hash.string_utils import zigZagConvert


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
        self.assertFalse(checkAnagrams(None, "abc"))
        self.assertFalse(checkAnagrams(None, None))


    def test_unequal_length(self):
        s1 = "abc"
        s2= "abca"
        result = checkAnagrams(s1, s2)
        self.assertFalse(result)

    def test_positive_case(self):
        s1 = "abcd"
        s2 = "dabc"
        result = checkAnagrams(s1, s2)
        self.assertTrue(result)
        s1 = "door"
        s2 = "odor"
        result2 = checkAnagrams(s1, s2)
        self.assertTrue(result2)

    def test_negative_case_extra_char(self):
        s1 = "abcd"
        s2 = "abce"
        res = checkAnagrams(s1, s2)
        self.assertFalse(res)

    def test_negative_case_unequal_number_of_chars(self):
        s3 = "aabb"
        s4 = "aaab"
        self.assertFalse(checkAnagrams(s3, s4))

    def test_neg_missing_char(self):
        s1 = "aaab"
        s2 = "bbaa"
        self.assertFalse(checkAnagrams(s1, s2))


class ZigZagConvertTest(unittest.TestCase):
    """
        Test string zig zag conversion
    """
    def setUp(self):
        pass

    def test_normal_case(self):
        """
            Test cases for zig zag conversion
        """
        self.assertEqual(zigZagConvert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zigZagConvert("ABC", 1), "ABC")

    # end of def

    def test_edge_cases(self):
        self.assertIsNone(zigZagConvert(None, 1))
        self.assertIsNone(zigZagConvert("ABC", -1))
# end of class


if __name__ == '__main__':
    unittest.main()
