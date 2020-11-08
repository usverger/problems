import unittest
from typing import List
import python.problems as problems

class Other(unittest.TestCase):

    def test_numWaterBottles(self):
        s = problems.WaterBottles.Solution()
        self.assertEqual(s.numWaterBottles(3, 2), 5)
        self.assertEqual(s.numWaterBottles(9, 3), 13)
        self.assertEqual(s.numWaterBottles(15, 4), 19)

    def test_climbStairsMinCost(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.climbStairsMinCost([10, 15, 20]), 15)
        self.assertEqual(s.climbStairsMinCost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        self.assertEqual(s.climbStairsMinCost([0, 0, 0, 0]), 0)
        self.assertEqual(s.climbStairsMinCost([0, 1, 1, 0]), 1)

    def test_climbStairs(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.climbStairs(38), 63245986)

    def test_largestTriangleArea(self):
        s = problems.LargestTriangleArea.Solution()
        self.assertEqual(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]), 2.0)
