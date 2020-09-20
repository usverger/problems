import unittest
from typing import List
import python.problems as problems

class Other(unittest.TestCase):

    def test_twoSum(self):
        s = problems.TwoSum.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [0,1])

    def test_twoSumSorted(self):
        s = problems.TwoSumSorted.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [1,2])
        
    def test_matrixCellsInDistanceOrder(self):
        s = problems.MatrixCellsInDistanceOrder.Solution()
        r = s.allCellsDistOrder(1,2, 0, 0)
        self.assertEqual(r, [[0,0], [0,1]])
        
    def test_reverseInteger(self):
        s = problems.ReverseInteger.Solution()
        r = s.reverse(123)
        self.assertEqual(r, 321)

    def test_palindromeNumber(self):
        s = problems.PalindromeNumber.Solution()

        r = s.isPalindrome(121)
        self.assertEqual(r, True)

        r = s.isPalindrome(10)
        self.assertEqual(r, False)


 
