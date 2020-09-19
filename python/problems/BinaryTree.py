from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        totalSum = 0
        stack = [(root, 0)] # first element of the tuple is the node, the second is path value before that node
        
        while stack:
            node, currentPathValue = stack.pop()
            if node is None:
                return totalSum

            currentPathValue = currentPathValue << 1 | node.val # shift left and plus another digit
            if not (node.left or node.right): # this is a leaf
                totalSum = totalSum + currentPathValue
            else:
                if node.left:
                    stack.append((node.left, currentPathValue))

                if node.right:  
                    stack.append((node.right, currentPathValue))
                    
        return totalSum
        
    def maxDepthIteration(self, root: TreeNode) -> int:
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

    def maxDepthRecursive(self, root: TreeNode) -> int:

        def traverse(node: TreeNode, current: int, maxDepth: int):
            if node is None:
                return maxDepth

            if node.left is None and node.right is None: # this is a leaf
                return max(maxDepth, current + 1)
            else:
                maxDepthLeft = traverse(node.left, current + 1, maxDepth)
                maxDepthRight = traverse(node.right, current + 1, maxDepth)
                return max(maxDepth, maxDepthLeft, maxDepthRight)

        return traverse(root, 0, 0)

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        minDepth = 2**31 - 1
        stack = [(root, 0)]
        while stack:
            node, currentPathLength = stack.pop()
            if node is None:
                return minDepth
            
            if node.left is None and node.right is None: # this is a leaf
                if currentPathLength + 1 < minDepth:
                    minDepth = currentPathLength + 1
            else:
                if node.left is not None:
                    stack.append((node.left, currentPathLength + 1))
                if node.right is not None:
                    stack.append((node.right, currentPathLength + 1))
                    
        return minDepth

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
        