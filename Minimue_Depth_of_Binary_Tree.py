# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None: return 0
        l1=self.minDepth(root.left)
        l2=self.minDepth(root.right)
        if l1==0 and l2==0:
            return 1
        if l1==0:
            return 1+l2
        if l2==0:
            return 1+l1
        return 1+min(l1,l2)
        
