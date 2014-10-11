# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def my_inorder(self,root,result):
        result[0].right=TreeNode(root.val)
        result[0].left=None
        result[0]=result[0].right
        if root.left!=None:
            self.my_inorder(root.left,result)
        if root.right!=None:
            self.my_inorder(root.right,result)
            
    def flatten(self, root):
        if root==None: return None
        myroot=TreeNode(0)
        head=myroot
        result=[myroot]
        self.my_inorder(root,result)
        root.left=None
        root.right=head.right.right
        
        
