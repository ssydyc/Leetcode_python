# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def my_hasPathSum(self,root,sum):
        if root.left==None and root.right==None:
            if sum==root.val:
                return True
            else:
                return False
        if root.left==None:
            return self.my_hasPathSum(root.right,sum-root.val)
        if root.right==None:
            return self.my_hasPathSum(root.left,sum-root.val)
        return self.my_hasPathSum(root.left,sum-root.val) or self.my_hasPathSum(root.right,sum-root.val)
        
    def hasPathSum(self, root, sum):
        if root==None: return False
        return self.my_hasPathSum(root,sum)
        
