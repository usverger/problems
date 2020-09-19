import unittest
from typing import List
import python.problems as problems

class Trees(unittest.TestCase):

    def test_sumofRootToLeafBinaryNumbers(self):
        s = problems.SumofRootToLeafBinaryNumbers.Solution()
        treeNode = s.generateTreeNode(None, 0, [1,0,1,0,1,0,1])
        
        r = s.sumRootToLeaf(treeNode)
        self.assertEqual(r, 22, 22)

    def test_maxDepth(self):
        s = problems.MaximumDepthOfBinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.maxDepth(treeNode)
        self.assertEqual(r, 3, 3)


 
