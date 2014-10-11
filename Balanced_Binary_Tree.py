# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def mylength(self,root,result):
        if not result[0]: return 0 # return anything if we know it's false
        if root==None: return 0
        l1=self.mylength(root.left,result)
        l2=self.mylength(root.right,result)
        if l1-l2>1 or l1-l2<-1:
            result[0]=False
            return 0
        return max(l1,l2)+1
    
    
    def isBalanced(self, root):
        result=[True]
        self.mylength(root,result)
        return result[0]
