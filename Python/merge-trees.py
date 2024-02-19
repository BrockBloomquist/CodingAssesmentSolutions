# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        Uses DFS specifically preorder traversal to merge trees by adding similarly positioned nodes
        and adding nodes that don't exist in the other tree at that position
        Time complexity O(n) Space complexity O(1)
        """
        if not root1:
            return root2
        if not root2:
            return root1

        m_root = TreeNode(root1.val + root2.val)
        m_root.left = self.mergeTrees(root1.left, root2.left)
        m_root.right = self.mergeTrees(root1.right, root2.right)
        
        return m_root