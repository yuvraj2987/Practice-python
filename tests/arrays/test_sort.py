import unittest

from arrays_and_hash import sort


class Merge(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_5_elm(self):
        tarr = [None] * 5
        arr1 = [2, 5, 7, 3, 4]
        ans1 = [2, 3, 4, 5, 7]
        sort.merge(arr1, tarr, 0, 2, 3, 4)
        self.assertEqual(arr1, ans1)
        arr2 = [2, 3, 4, 5, 7]
        sort.merge(arr2, tarr, 0, 2, 3, 4)
        self.assertEqual(arr2, ans1)
        arr3 = [4, 5, 7, 2, 3]
        sort.merge(arr3, tarr, 0, 2, 3, 4)
        self.assertEqual(arr3, ans1)

    def test_merge_4_elm(self):
        tarr = [None] * 4
        arr1 = [1, 4, 2, 3]
        ans  = [1, 2, 3, 4]
        sort.merge(arr1, tarr, 0, 1, 2, 3)
        self.assertEqual(arr1, ans)
        arr2 = [1, 2, 3, 4]
        sort.merge(arr2, tarr, 0, 1, 2, 3)
        self.assertEqual(arr2, ans)
        arr3 = [3, 4, 1, 2]
        sort.merge(arr3, tarr, 0, 1, 2, 3)
        self.assertEqual(arr3, ans)


    def test_merge_3_elm(self):
        tarr = [None] * 3
        arr1 = [1, 3, 2]
        ans = [1, 2, 3]
        sort.merge(arr1, tarr, 0, 1, 2, 2)
        self.assertEqual(arr1, ans)
        arr2 = [2, 3, 1]
        sort.merge(arr2, tarr, 0, 1, 2, 2)
        self.assertEqual(arr2, ans)

    def test_merge_2_elm(self):
        tarr = [None] * 2
        arr1 = [6, 2]
        ans1 = [2, 6]
        sort.merge(arr1, tarr, 0, 0, 1, 1)
        self.assertEqual(arr1, ans1)
        arr2 = [6, 2]
        sort.merge(arr2, tarr, 0, 0, 1, 1)
        self.assertEqual(arr2, ans1)

    def test_merge_1_elm(self):
        tarr = [None]
        arr1 = [3]
        ans1 = [3]
        sort.merge(arr1, tarr, 0, 0, 0, 0)
        self.assertEqual(arr1, ans1)
        arr2 = [1, 2, 3, 4]
        ans2 = [1, 2, 3, 4]
        sort.merge(arr2, tarr, 3, 3 ,3 ,3)
        self.assertEqual(arr2, ans2)

    def test_merge_invalid(self):
        tarr = [None] * 4
        arr = [1, 4, 2, 3]
        ans = [1, 4, 2, 3]
        sort.merge(arr, tarr, 4, 3, 1, 2)
        self.assertEqual(arr, ans)
        sort.merge(arr, tarr, 1, 2, 1, 2)
        self.assertEqual(arr, ans)
# End of class

class TestMergeRecur(unittest.TestCase):

    def setUp(self):
        pass

    def test_4_elm(self):
        arr1 = [4, 1, 2, 3]
        ans  = [1, 2, 3, 4]
        tarr = [None] * 4
        sort.mergeRecur(arr1, tarr, 0, 3)
        self.assertEqual(arr1, ans)
        arr2 = [4, 3, 2, 1]
        sort.mergeRecur(arr2, tarr, 0, 3)
        self.assertEqual(arr2, ans)
        arr3 = [1, 2, 3, 4]
        sort.mergeRecur(arr3, tarr, 0, 3)
        self.assertEqual(arr3, ans)

    def test_2_elm(self):
        arr1 = [4, 3]
        ans = [3, 4]
        tarr = [None] * 2
        sort.mergeRecur(arr1, tarr, 0, 1)
        self.assertEqual(arr1, ans)
        arr2 = [4, 3]
        sort.mergeRecur(arr2, tarr, 0, 1)
        self.assertEqual(arr2, ans)

    def test_1_elm(self):
        arr1 = [3]
        tarr = []
        ans  = [3]
        sort.mergeRecur(arr1, tarr, 0, 0)
        self.assertEqual(arr1, ans)

    def test_5_elm(self):
        arr1 = [4, 3, 7, 2, 5]
        ans  = [2, 3, 4, 5, 7]
        tarr = [None] * 5
        sort.mergeRecur(arr1, tarr, 0, 4)
        self.assertEqual(arr1, ans)
        arr2 = [ 7, 5, 4, 3, 2]
        sort.mergeRecur(arr2, tarr, 0, 4)
        self.assertEqual(arr2, ans)



if __name__ == '__main__':
    unittest.main()
