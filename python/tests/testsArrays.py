import unittest
from typing import List
import python.problems as problems

class Arrays(unittest.TestCase):

    def test_addBinary(self):
        s = problems.Arrays.Solution()

        self.assertEqual(s.addBinary('0', '0'), '0') 
        self.assertEqual(s.addBinary('11', '1'), '100')
        self.assertEqual(s.addBinary('1010', '1011'), '10101')

    def test_addStrings(self):
        s = problems.Arrays.Solution()

        self.assertEqual(s.addStrings('0', '0'), '0') 
        self.assertEqual(s.addStrings('1', '9'), '10')
        self.assertEqual(s.addStrings('9', '9'), '18')
        self.assertEqual(s.addStrings('9', '999'), '1008')

    def test_plusOne(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(s.plusOne([0]), [1])
        self.assertEqual(s.plusOne([1]), [2])
        self.assertEqual(s.plusOne([9,9,9]), [1,0,0,0])

    def test_dominantIndex(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.dominantIndex([3, 6, 1, 0]), 1)
        self.assertEqual(s.dominantIndex([1,2,3,4]), -1)
        self.assertEqual(s.dominantIndex([]), -1)

    def test_pivotIndex(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.pivotIndex([1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex([1,2,3]), -1)
        self.assertEqual(s.pivotIndex([]), -1)

    def test_numIdenticalPairs(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3]), 0)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_Linear([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3]), 0)

    def test_sumOddLengthSubarrays(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,4,2,5,3]), 58)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,2]), 3)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([10,11,12]), 66)

    def test_moveZeroes(self):
        s = problems.Arrays.Solution()

        arr = [0,1,0,3,12]
        s.moveZeroes(arr)
        self.assertEqual(arr, [1,3,12,0,0])

        arr = [0,1]
        s.moveZeroes(arr)
        self.assertEqual(arr, [1,0])
