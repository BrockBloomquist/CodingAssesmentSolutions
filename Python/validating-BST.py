# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#   Time complexity O(n) Space Complexity O(h) where h is the height of the tree
class Solution(object):
    def helper(self, l, left, right):
        if not l:
            return True
        if not (l.val < right and l.val > left):
            return False
        return self.helper(l.left, left, l.val) and self.helper(l.right, l.val, right)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float("-inf"), float("inf"))
        