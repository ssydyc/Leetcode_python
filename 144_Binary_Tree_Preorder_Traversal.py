# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
        self.stack=[]
    
    def leftMost(self,root,result):
        while root:
            self.stack.append(root)
            result.append(root.val)
            root=root.left
        
    def preorderTraversal(self, root):
        result=[]
        self.leftMost(root,result)
        while self.stack:
            temp=self.stack.pop()
            if temp.right:
                self.leftMost(temp.right,result)
        return result
        
        
