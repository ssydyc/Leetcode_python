# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def inorder_traverse(self,root,result):
        if root.left!=None:
            self.inorder_traverse(root.left,result)
        if result[0]!=None:
            if result[0].val>root.val: # problems now
                if result[1]==None:
                    result[1]=result[0]
                    result[2]=root
                else:
                    result[2]=root
        result[0]=root #change previous node
        if root.right!=None:
            self.inorder_traverse(root.right,result)
    
    def recoverTree(self, root):
        if root==None: return root
        result=[None,None,None] #prev, first and second
        self.inorder_traverse(root,result) #record first and second node
        if result[1]!=None and result[2]!=None:
            result[1].val,result[2].val=result[2].val,result[1].val
        return root
