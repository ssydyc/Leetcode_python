# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        result=[]
        if root==None: return result
        level_stack=[root]
        direction=False
        while len(level_stack)!=0:
            temp_level=[] # output result
            temp_stack=[] #store the temp_stack
            for j in range(len(level_stack)):
                temp=level_stack.pop()
                if direction:
                    if temp.right!=None:
                        temp_stack.append(temp.right)
                    if temp.left!=None:
                        temp_stack.append(temp.left)
                else:
                    if temp.left!=None:
                        temp_stack.append(temp.left)
                    if temp.right!=None:
                        temp_stack.append(temp.right)
                temp_level.append(temp.val)
            direction=not direction
            result.append(temp_level)
            level_stack,temp_stack=temp_stack, level_stack
        return result
                
