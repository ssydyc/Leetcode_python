# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def post_order(self,root,result_post):
        result_post.append(root.val)
        if root.right!=None:
            self.post_order(root.right,result_post)
        else:
            result_post.append(None)
        if root.left!=None:
            self.post_order(root.left,result_post)
        else:    
            result_post.append(None)
            
    def pre_order(self,root,result_pre):
        result_pre.append(root.val)
        if root.left!=None:
            self.pre_order(root.left,result_pre)
        else:
            result_pre.append(None)
        if root.right!=None:
            self.pre_order(root.right,result_pre)
        else:
            result_pre.append(None)
        
    def isSymmetric(self, root):
        if root==None: return True
        if root.left==None and root.right==None: return True
        if root.left==None or root.right==None: return False
        result_post=[]
        result_pre=[]
        self.post_order(root.left,result_post)
        self.pre_order(root.right,result_pre)
        if result_post==result_pre:
            return True
        else:
            return False
