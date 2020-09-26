import unittest
from typing import List
import python.problems as problems

class Arrays(unittest.TestCase):

    def test_pivotIndex(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.pivotIndex([1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex([1,2,3]), -1)

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
