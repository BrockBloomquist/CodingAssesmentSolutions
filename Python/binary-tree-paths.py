# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(n) Space Complexity O(n) (recursive stack space)
class Solution(object):
    # Function to print preorder traversal
    def preorder(self, node, res, curPath):
        if node and not node.left and not node.right:
            curPath += str(node.val)
            res.append(curPath)
            return
        curPath += str(node.val) + "->"
        if node.left:
            self.preorder(node.left, res, curPath)
        if node.right:
            self.preorder(node.right, res, curPath)
        

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        curPath = ""
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        self.preorder(root, res, curPath)
        return res