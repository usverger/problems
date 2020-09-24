import unittest
from typing import List
import python.problems as problems

class Other(unittest.TestCase):

    def test_numIdenticalPairs(self):
        s = problems.NumberOfGoodPairs.Solution()
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3]), 0)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_Linear([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3]), 0)

    def test_sumOddLengthSubarrays(self):
        s = problems.SumOddLengthSubarrays.Solution()
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,4,2,5,3]), 58)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,2]), 3)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([10,11,12]), 66)

    def test_addStrings(self):
        s = problems.AddStrings.Solution()

        r = s.addStrings('0', '0')
        self.assertEqual(r, '0')
        r = s.addStrings('1', '9')
        self.assertEqual(r, '10')
        r = s.addStrings('9', '9')
        self.assertEqual(r, '18')
        r = s.addStrings('9', '999')
        self.assertEqual(r, '1008')

    def test_moveZeroes(self):
        s = problems.MoveZeroes.Solution()

        arr = [0,1,0,3,12]
        s.moveZeroes(arr)
        self.assertEqual(arr, [1,3,12,0,0])

        arr = [0,1]
        r = s.moveZeroes(arr)
        self.assertEqual(arr, [1,0])

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


 
