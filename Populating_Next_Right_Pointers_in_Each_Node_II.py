# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root==None: return
        temp=root.next
        Next=None
        while temp!=None:
            if temp.left:
                Next=temp.left
                break
            if temp.right:
                Next=temp.right
                break
            temp=temp.next
        if root.right:
            root.right.next=Next
            if root.left:
                root.left.next=root.right
        else:
            if root.left:
                root.left.next=Next
            
        if root.right:
            self.connect(root.right)
        if root.left:
            self.connect(root.left)
