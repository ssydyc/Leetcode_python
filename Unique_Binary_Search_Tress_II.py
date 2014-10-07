# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def my_generateTrees(self,start,end):
        result=[]
        if start>end: # nothing
            return [None]
        for i in range(start,end+1):
            for j in self.my_generateTrees(start,i-1):
                for k in self.my_generateTrees(i+1,end):
                    root=TreeNode(i)
                    root.left=j
                    root.right=k
                    result.append(root)
        return result
    
    def generateTrees(self, n):
        return self.my_generateTrees(1,n) #we need to add a inital number here and number of nodes
