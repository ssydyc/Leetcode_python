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
        self.stack=[] # we need a stack to store nodes
    
    def update_stack(self,root):
        # update the stack from root
        self.stack.append(root)
        while root.left or root.right:
            while root.left:
                root=root.left
                self.stack.append(root)
            if root.right:
                root=root.right
                self.stack.append(root)
    
    def findNext(self):
        result=self.stack.pop() # the last one in stack is the result
        if not self.stack: return result # it's the last one, root
        if result==self.stack[len(self.stack)-1].left:
            if self.stack[len(self.stack)-1].right:
                self.update_stack(self.stack[len(self.stack)-1].right)
        return result
        
    def postorderTraversal(self, root):
        if not root: return []
        result=[]
        self.update_stack(root)
        while self.stack:
            result.append(self.findNext().val)
        return result
        
