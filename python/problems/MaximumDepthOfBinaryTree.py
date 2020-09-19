from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxDepth = 0
        
        stack = [(root, 0)]
        
        while stack:
            node, current = stack.pop()
            if node is None:
                return maxDepth
            
            if not (node.left or node.right): # this is a leaf
                if maxDepth < current + 1:
                    maxDepth = current + 1             
            else:
                if node.left:
                    stack.append((node.left, current + 1))

                if node.right:  
                    stack.append((node.right, current + 1))
        
        return maxDepth

    def generateTreeNode(self, root: TreeNode, index: int, values: List[int]):

        # for each generation
        # start index: 2**level - 1
        # length 2**level

        # for each node index i its children are located at 2*i+1 and 2*i+2

        if index < len(values) and values[index] is not None:
            root = TreeNode(values[index])
            root.left = self.generateTreeNode(root.left, 2 * index + 1, values)
            root.right = self.generateTreeNode(root.right, 2 * index + 2, values)
        return root
        