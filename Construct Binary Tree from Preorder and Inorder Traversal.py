# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def my_buildTree(self,preorder,pre_lower,pre_upper,inorder,in_lower): #with upper bound and lower bound
        if pre_lower>pre_upper or in_lower>len(inorder)-1: return None
        temp=inorder[in_lower]
        for i in range(pre_lower,pre_upper+1): #search preorder tree
            if preorder[i]==temp: #now we found the in order one
                root=TreeNode(temp) # the first inorder
                root.left=self.my_buildTree(preorder,pre_lower,i-1,inorder,in_lower+1)
                root.right=self.my_buildTree(preorder,i+1,pre_upper,inorder,in_lower+i-pre_lower+1)
                return root
                break
        
    def buildTree(self, preorder, inorder):
        return self.my_buildTree(inorder,0,len(preorder)-1,preorder,0)
