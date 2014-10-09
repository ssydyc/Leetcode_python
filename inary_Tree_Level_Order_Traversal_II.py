# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result=[]
        if root==None: return result
        level_queue=collections.deque([root])
        while len(level_queue)!=0:
            temp_level=[]
            for j in range(len(level_queue)):
                temp=level_queue.popleft()
                if temp.left!=None:
                    level_queue.append(temp.left)
                if temp.right!=None:
                    level_queue.append(temp.right)
                temp_level.append(temp.val)
            result.append(temp_level)
        final_result=[]
        for i in range(len(result)):
            final_result.append(result.pop())
        return final_result
