import unittest
from typing import List
import python.leetcode as leetcode

class Trees(unittest.TestCase):

    def test_isSymmetric(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [1,2,2,3,4,4,3])
        self.assertEqual(s.isSymmetricRecursive(treeNode), True)
        self.assertEqual(s.isSymmetricIteration(treeNode), True)

        treeNode = s.generateTreeNode(None, 0, [1,2,2,None,3,None,3])
        self.assertEqual(s.isSymmetricRecursive(treeNode), False)
        self.assertEqual(s.isSymmetricIteration(treeNode), False)

        treeNode = s.generateTreeNode(None, 0, [1,2,2,None,3,3,None])
        self.assertEqual(s.isSymmetricRecursive(treeNode), True)
        self.assertEqual(s.isSymmetricIteration(treeNode), True)

    def test_sortedArrayToBST(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.sortedArrayToBST([-10,-3,0,5,9])
        self.assertEqual(s.printInLevelOrder(treeNode), [0,-3,9,-10,None,5])

    def test_printInLevelOrder(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        self.assertEqual(s.printInLevelOrder(treeNode), [3,9,20,None,None,15,7])

    def test_isValidBST(self):
        s = leetcode.BinaryTree.Solution()

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
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [1,0,1,0,1,0,1])
        
        r = s.sumRootToLeaf(treeNode)
        self.assertEqual(r, 22)

    def test_maxDepthIteration(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.maxDepthIteration(treeNode)
        self.assertEqual(r, 3)

    def test_maxDepthRecursive(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.maxDepthRecursive(treeNode)
        self.assertEqual(r, 3)

    def test_maxDepthRecursiveEmpty(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [])
        
        r = s.maxDepthRecursive(treeNode)
        self.assertEqual(r, 0)

    def test_minDepth(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.minDepth(treeNode)
        self.assertEqual(r, 2)

    def test_levelOrder(self):
        s = leetcode.BinaryTree.Solution()
        treeNode = s.generateTreeNode(None, 0, [3,9,20,None,None,15,7])
        
        r = s.levelOrder(treeNode)
        self.assertEqual(r, [[3],[9,20],[15,7]])

    def test_inOrderTraversalRecursive(self):
        s = leetcode.BinaryTree.Solution()

        r = s.inorderTraversalRecursive(s.generateTreeNode(None, 0, [1,None,2,None,None,3,None]))
        self.assertEqual(r, [1,3,2])

        r = s.inorderTraversalRecursive(s.generateTreeNode(None, 0, []))
        self.assertEqual(r, [])

        r = s.inorderTraversalRecursive(s.generateTreeNode(None, 0, [1,2]))
        self.assertEqual(r, [2,1])
 
        r = s.inorderTraversalRecursive(s.generateTreeNode(None, 0, [1,None,2]))
        self.assertEqual(r, [1,2])

    def test_inOrderTraversalIteration(self):
        s = leetcode.BinaryTree.Solution()

        r = s.inorderTraversalIteration(s.generateTreeNode(None, 0, [1,None,2,None,None,3,None]))
        self.assertEqual(r, [1,3,2])

        r = s.inorderTraversalIteration(s.generateTreeNode(None, 0, []))
        self.assertEqual(r, [])

        r = s.inorderTraversalIteration(s.generateTreeNode(None, 0, [1,2]))
        self.assertEqual(r, [2,1])
 
        r = s.inorderTraversalIteration(s.generateTreeNode(None, 0, [1,None,2]))
        self.assertEqual(r, [1,2])

