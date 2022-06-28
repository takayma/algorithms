import unittest
import random
from sort.insertion_sort.insertion_sort import insertion_sort as srt


class Test(unittest.TestCase):
    def test_sort1(self):
        arr = [1, -1, 3, 9, 0, 0, 4, 2, -5]
        arr1 = arr.copy()
        arr2 = arr.copy()
        arr1.sort()
        self.assertEqual(srt(arr), arr1)
        self.assertEqual(arr, arr2)

    def test_sort2(self):
        arr = [random.randint(-100, 100) for i in range(100)]
        arr1 = arr.copy()
        arr2 = arr.copy()
        arr1.sort()
        self.assertEqual(srt(arr), arr1)
        self.assertEqual(arr, arr2)


if __name__ == '__main__':
    unittest.main()
