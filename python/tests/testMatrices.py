import unittest
from typing import List
import python.leetcode as leetcode

class Matrices(unittest.TestCase):

    def test_validSudoku(self):
        s = leetcode.Matrices.Solution()
        self.assertEqual(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]), True)
        self.assertEqual(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]), False)

    def test_rotate(self):
        s = leetcode.Matrices.Solution()
        self.assertEqual(s.rotate([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
        self.assertEqual(s.rotate([[1]]), [[1]])
        self.assertEqual(s.rotate([[1,2],[3,4]]), [[3,1],[4,2]])

    def test_pascalTriangle(self):
        s = leetcode.Matrices.Solution()
        self.assertEqual(s.pascalTriangle(1), [[1]])
        self.assertEqual(s.pascalTriangle(2), [[1], [1,1]])
        self.assertEqual(s.pascalTriangle(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        self.assertEqual(s.pascalTriangle_WithPaddedArrays(1), [[1]])
        self.assertEqual(s.pascalTriangle_WithPaddedArrays(2), [[1], [1,1]])
        self.assertEqual(s.pascalTriangle_WithPaddedArrays(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_spiralOrder(self):
        s = leetcode.Matrices.Solution()
        
        self.assertEqual(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(s.spiralOrder([]), [])
        self.assertEqual(s.spiralOrder([[]]), [])
        self.assertEqual(s.spiralOrder([[1,2],[3,4]]), [1,2,4,3])
        self.assertEqual(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])

    def test_findDiagonalOrder_WithMap(self):
        s = leetcode.Matrices.Solution()
        
        self.assertEqual(s.findDiagonalOrder_WithMap([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(s.findDiagonalOrder_WithMap([]), [])
        self.assertEqual(s.findDiagonalOrder_WithMap([[]]), [])
        self.assertEqual(s.findDiagonalOrder_WithMap([[0]]), [0])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2,3]]), [2,3])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2,3,4]]), [2,3,4])
        self.assertEqual(s.findDiagonalOrder_WithMap([[2],[3],[4]]), [2,3,4])

    def test_findDiagonalOrder(self):
        s = leetcode.Matrices.Solution()
        
        self.assertEqual(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(s.findDiagonalOrder([]), [])
        self.assertEqual(s.findDiagonalOrder([[]]), [])
        self.assertEqual(s.findDiagonalOrder([[0]]), [0])
        self.assertEqual(s.findDiagonalOrder([[2,3]]), [2,3])
        self.assertEqual(s.findDiagonalOrder([[2,3,4]]), [2,3,4])
        self.assertEqual(s.findDiagonalOrder([[2],[3],[4]]), [2,3,4])

    def test_matrixCellsInDistanceOrder(self):
        s = leetcode.Matrices.Solution()
        self.assertEqual(s.allCellsDistOrder(1,2, 0, 0), [[0,0], [0,1]])
     