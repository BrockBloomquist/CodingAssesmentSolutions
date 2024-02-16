# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n) Space complexity: O(n) recursive stack space in python memory
class Solution(object):
    def printPostorder(self, node):
        if node is None:
            return
    
        # First recur on left subtree
        self.printPostorder(node.left)
    
        # Then recur on right subtree
        self.printPostorder(node.right)
    
        if not node.left and not node.right:
            return
        tmp = node.left
        node.left = node.right
        node.right = tmp
        return node

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.printPostorder(root)
        return root