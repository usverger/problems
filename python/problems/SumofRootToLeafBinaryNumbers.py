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
            currentPathValue = currentPathValue << 1 | node.val # shift left and plus another digit
            if not (node.left or node.right): # this is a leaf
                totalSum = totalSum + currentPathValue
            else:
                if node.left:
                    stack.append((node.left, currentPathValue))

                if node.right:  
                    stack.append((node.right, currentPathValue))
                    
        return totalSum

    def generateTreeNode(self, root: TreeNode, index: int, values: List[int]):

        # for each generation
        # start index: 2**level - 1
        # length 2**level

        # for each node index i its children are located at 2*i+1 and 2*i+2

        if index < len(values):
            root = TreeNode(values[index])
            root.left = self.generateTreeNode(root.left, 2 * index + 1, values)
            root.right = self.generateTreeNode(root.right, 2 * index + 2, values)
        return root
        