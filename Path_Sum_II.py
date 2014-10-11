# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    
    def my_hasPathSum(self,root,sum,temp,result):
        if root.left==None and root.right==None:
            if sum==root.val:
                temp.append(root.val)
                result.append(list(temp))
                temp.pop()
                return
            else:
                return
        if root.left==None:
            temp.append(root.val)
            self.my_hasPathSum(root.right,sum-root.val,temp,result)
            temp.pop()
            return
        if root.right==None:
            temp.append(root.val)
            self.my_hasPathSum(root.left,sum-root.val,temp,result)
            temp.pop()
            return
        temp.append(root.val)
        self.my_hasPathSum(root.right,sum-root.val,temp,result)
        self.my_hasPathSum(root.left,sum-root.val,temp,result)
        temp.pop()
        
        
    def pathSum(self, root, sum):
        if root==None: return []
        temp,result=[],[] # define a list for use
        self.my_hasPathSum(root,sum,temp,result)
        return result
        
        
        
        
