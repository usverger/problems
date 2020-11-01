using System.Linq;
using System.Collections.Generic;

namespace Problems
{
    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class Trees
    {
        public int MaxDepth(TreeNode root) {
            
            if (root == null) return 0;
            
            int max = 0;
            var stack = new Stack<(TreeNode, int)>();
            stack.Push((root, 0));
            
            while (stack.Count > 0)
            {
                (TreeNode node, int depth) t = stack.Pop();
                
                if (t.node.left == null && t.node.right == null)
                {
                    if (max < t.depth + 1) max = t.depth + 1;
                }
                else
                {
                    if (t.node.left != null) {
                        stack.Push((t.node.left, t.depth + 1));
                    }
                    
                    if (t.node.right != null) {
                        stack.Push((t.node.right, t.depth + 1));
                    }
                }
            }
            
            return max;
        }

        public TreeNode GenerateTreeNode(TreeNode root, int index, List<int?> values)
        {
            if (index < values.Count && values[index] != null)
            {
                root = new TreeNode(values[index].Value);
                root.left = GenerateTreeNode(root.left, 2 * index + 1, values);
                root.right = GenerateTreeNode(root.right, 2 * index + 2, values);
            }
            return root;
        }
    }
}