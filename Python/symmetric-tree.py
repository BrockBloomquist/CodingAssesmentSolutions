# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)