# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
        
    def maxRootLeaf(self, root):
        if root is None: return 0
        lmax = self.maxRootLeaf(root.left)
        rmax = self.maxRootLeaf(root.right)
        self.res = max(self.res, max(lmax, 0) + max(rmax, 0) + root.val)
        return max(lmax, rmax, 0) + root.val
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.res = root.val
        self.maxRootLeaf(root)
        return self.res
