import unittest
from typing import List
import python.problems as problems

class Trees(unittest.TestCase):

    def test_isValidBST(self):
        s = problems.BinaryTree.Solution()

        treeNode = s.generateTreeNode(None, 0, [2147483647])   
        self.assertLess(2147483647, float('inf'))      
        self.assertEqual(s.isValidBSTRecursive(treeNode), True)
        self.assertEqual(s.isValidBSTIteration(treeNode), True)

        treeNode = s.generateTreeNode(None, 0, [])   
        self.assertEqual(s.isValidBSTRecursive(treeNode), True)
        self.assertEqual(s.isValidBSTIteration(treeNode), True)

        treeNode = s.generateTreeNode(None, 0, [2,1,3])   
        self.assertEqual(s.isValidBSTRecursive(treeNode), True)
        self.assertEqual(s.isValidBSTIteration(treeNode), True)

        treeNode = s.generateTreeNode(None, 0, [5,1,4,None,None,3,6])
        self.assertEqual(s.isValidBSTRecursive(treeNode), False)
        self.assertEqual(s.isValidBSTIteration(treeNode), False)

        treeNode = s.generateTreeNode(None, 0, [10,5,15,None,None,6,20])
        self.assertEqual(s.isValidBSTRecursive(treeNode), False)
        self.assertEqual(s.isValidBSTIteration(treeNode), False)

    def test_sumofRootToLeafBinaryNumbers(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [1,0,1,0,1,0,1])
        
        r = s.sumRootToLeaf(treeNode)
        self.assertEqual(r, 22)

    def test_maxDepthIteration(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.maxDepthIteration(treeNode)
        self.assertEqual(r, 3)

    def test_maxDepthRecursive(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.maxDepthRecursive(treeNode)
        self.assertEqual(r, 3)

    def test_maxDepthRecursiveEmpty(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [])
        
        r = s.maxDepthRecursive(treeNode)
        self.assertEqual(r, 0)

    def test_minDepth(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.minDepth(treeNode)
        self.assertEqual(r, 2)

    def test_levelOrder(self):
        s = problems.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.levelOrder(treeNode)
        self.assertEqual(r, [[3],[9,20],[15,7]])


 
