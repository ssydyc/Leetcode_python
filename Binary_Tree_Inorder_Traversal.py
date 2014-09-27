# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def myTraversal(self,root,result):
        if root.left==None:
            result.append(root.val)
            if root.right!=None:
                self.myTraversal(root.right,result)
        else:
            self.myTraversal(root.left,result)
            result.append(root.val)
            if root.right!=None:
                self.myTraversal(root.right,result)
            
    def inorderTraversal(self, root):
        if root==None: return []
        result=[]
        self.myTraversal(root,result)
        return result
