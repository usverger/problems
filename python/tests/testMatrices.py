import unittest
from typing import List
import python.problems as problems

class Matrices(unittest.TestCase):

    def test_findDiagonalOrder_WithMap(self):
        s = problems.Matrices.Solution()
        
        self.assertEqual(s.findDiagonalOrder_WithMap([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(s.findDiagonalOrder_WithMap([]), [])
        self.assertEqual(s.findDiagonalOrder_WithMap([[]]), [])
        self.assertEqual(s.findDiagonalOrder_WithMap([[0]]), [0])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2,3]]), [2,3])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2,3,4]]), [2,3,4])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2],[3],[4]]), [2,3,4])

    def test_findDiagonalOrder(self):
        s = problems.Matrices.Solution()
        
        self.assertEqual(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(s.findDiagonalOrder([]), [])
        self.assertEqual(s.findDiagonalOrder([[]]), [])
        self.assertEqual(s.findDiagonalOrder([[0]]), [0])
        self.assertEqual(s.findDiagonalOrder([[2,3]]), [2,3])
        self.assertEqual(s.findDiagonalOrder([[2,3,4]]), [2,3,4])
        self.assertEqual(s.findDiagonalOrder([[2],[3],[4]]), [2,3,4])

    def test_matrixCellsInDistanceOrder(self):
        s = problems.Matrices.Solution()
        self.assertEqual(s.allCellsDistOrder(1,2, 0, 0), [[0,0], [0,1]])
     