import unittest
import python.problems as problems

class TestFixture(unittest.TestCase):

    def test_twoSum(self):
        s = problems.TwoSum.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [0,1])

    def test_twoSumSorted(self):
        s = problems.TwoSumSorted.Solution()
        r = s.twoSum([2,7,11,15], 9)
        self.assertEqual(r, [1,2])

    def test_restoreString(self):
        s = problems.RestoreString.Solution()
        r = s.restoreString("codeleet", [4,5,6,7,0,2,1,3])
        self.assertEqual(r, "leetcode")

    def test_matrixCellsInDistanceOrder(self):
        s = problems.MatrixCellsInDistanceOrder.Solution()
        r = s.allCellsDistOrder(1,2, 0, 0)
        self.assertEqual(r, [[0,0], [0,1]])

    def test_reverseInteger(self):
        s = problems.ReverseInteger.Solution()
        r = s.reverse(123)
        self.assertEqual(r, 321)


 
