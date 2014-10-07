# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def my_isValidBST(self, root, lower, upper):
        if root==None: return True
        if root.val<=lower or root.val>=upper:
            return False
        if root.left!=None and not self.my_isValidBST(root.left, lower, min(root.val,upper)):
            return False
        if root.right!=None and not self.my_isValidBST(root.right, max(lower,root.val),upper):
            return False
        return True
        
    def isValidBST(self, root):
        return self.my_isValidBST(root,float('-Inf'),float('Inf')) # test with bound
        
        
