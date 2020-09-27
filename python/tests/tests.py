import unittest
from typing import List
import python.problems as problems

class Other(unittest.TestCase):

    def test_numWaterBottles(self):
        s = problems.WaterBottles.Solution()
        self.assertEqual(s.numWaterBottles(3, 2), 5)
        self.assertEqual(s.numWaterBottles(9, 3), 13)
        self.assertEqual(s.numWaterBottles(15, 4), 19)

    def test_climbStairs(self):
        s = problems.ClimbStairs.Solution()
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.climbStairs(38), 63245986)

    def test_largestTriangleArea(self):
        s = problems.LargestTriangleArea.Solution()
        self.assertEqual(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]), 2.0)

    def test_twoSum(self):
        s = problems.TwoSum.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [0,1])

    def test_twoSumSorted(self):
        s = problems.TwoSumSorted.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [1,2])
