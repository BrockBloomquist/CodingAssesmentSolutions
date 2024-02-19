# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#   Time Complexity O(n) Space Complexity O(n)
class Solution(object):
    def findLeaf_dfs(self, leaf, v):
        if not leaf:
            return
        if not leaf.left and not leaf.right:
            v.append(leaf.val)
            return
        else:
            self.findLeaf_dfs(leaf.left, v)
            self.findLeaf_dfs(leaf.right, v)
        

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        nodeList1 = []
        nodeList2 = []
        self.findLeaf_dfs(root1, nodeList1)
        self.findLeaf_dfs(root2, nodeList2)
        
        return nodeList1 == nodeList2
        