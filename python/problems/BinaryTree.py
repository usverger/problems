from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        def helper(nums: List[int], l: int, r: int) -> TreeNode:
            if r - l == 0: return None
            
            mid = (r - l) // 2 + l
            root = TreeNode(nums[mid])
            root.left = helper(nums, l, mid)
            root.right = helper(nums, mid + 1, r)
            return root
        
        node = helper(nums, 0, len(nums))
        return node

    def isValidBSTIteration(self, root: TreeNode) -> bool:
        if not root: return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, min, max = stack.pop()
            if node.val <= min or node.val >= max: return False
            if node.left: stack.append((node.left, min, node.val))
            if node.right: stack.append((node.right, node.val, max))
        return True

    def isValidBSTRecursive(self, root: TreeNode) -> bool:

        def isValidBST(root: TreeNode, minimum: int, maximum: int) -> bool:
            if not root: return True
            if root.val <= minimum or root.val >= maximum: return False

            if not isValidBST(root.left, minimum, root.val): return False
            if not isValidBST(root.right, root.val, maximum): return False
            return True
        
        return isValidBST(root, float('-inf'), float('inf'))

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

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        q = []
        q.append((root, 0)) # q will contain the node candidates to traverse along with their level number
        
        while q:            
            n = q.pop(0) # take the next node
            if n[0] is not None:
                
                # visit the current node by building the result
                if n[1] > len(result) - 1:
                    result.append([])
                    
                result[n[1]].append(n[0].val)
                
                # discover the child nodes and append to the candidates queue
                q.append((n[0].left, n[1] + 1))
                q.append((n[0].right, n[1] + 1))
        
        return result

    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode, result: List[int]):
            if root.left: helper(root.left, result)
            result.append(root.val)
            if root.right: helper(root.right, result)

        result = []
        if not root: return result
        helper(root, result)
        return result

    def inorderTraversalIteration(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []

        discovered = set()
        q = deque([root])
        while q:

            # get the next candidate
            node = q.popleft()
            if node not in discovered:
                # discover
                if node.right: q.appendleft(node.right)
                q.appendleft(node)
                if node.left: q.appendleft(node.left)
                discovered.add(node)
            else:
                # visit by appending
                result.append(node.val)

        return result

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
        
    def printInLevelOrder(self, root: TreeNode) -> List[int]:
        result = []
        q = []
        q.append(root)
        while q:            
            n = q.pop(0)
            result.append(n.val if n is not None else None)
            if n is not None:
                q.append(n.left)
                q.append(n.right)
        
        while not result[-1]: result.pop()
        return result

        
