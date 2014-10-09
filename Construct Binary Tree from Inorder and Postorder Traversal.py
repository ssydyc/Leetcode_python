# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def my_buildTree(self,inorder,in_lower,in_upper,postorder,post_upper): #with upper bound and lower bound
        if in_lower>in_upper: return None
        temp=postorder[post_upper]
        i=inorder.index(temp)
        root=TreeNode(temp) # the first inorder
        root.left=self.my_buildTree(inorder,in_lower,i-1,postorder,post_upper-1-(in_upper-i-1)-1)
        root.right=self.my_buildTree(inorder,i+1,in_upper,postorder,post_upper-1)
        return root
    
    
    def buildTree(self, inorder, postorder):
        return self.my_buildTree(inorder,0,len(inorder)-1,postorder,len(postorder)-1)
