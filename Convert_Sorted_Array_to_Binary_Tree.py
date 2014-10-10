# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def my_sortedArrayToBST(self,num,lower,upper):
        if lower>upper: return None
        temp_index=(lower+upper+1)/2
        root=TreeNode(num[temp_index])
        root.left=self.my_sortedArrayToBST(num,lower,temp_index-1)
        root.right=self.my_sortedArrayToBST(num,temp_index+1,upper)
        return root
    
    def sortedArrayToBST(self, num):
        return self.my_sortedArrayToBST(num,0,len(num)-1)
