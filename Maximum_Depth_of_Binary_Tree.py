# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        level=0
        if root==None: return level
        level_queue=collections.deque([root])
        while len(level_queue)!=0:
            level+=1
            for j in range(len(level_queue)):
                temp=level_queue.popleft()
                if temp.left!=None:
                    level_queue.append(temp.left)
                if temp.right!=None:
                    level_queue.append(temp.right)
        return level
