# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, ind, trange):
        if ind > trange[1]: trange[1] = ind
        if ind < trange[0]: trange[0] = ind
        if root.left: self.inorder(root.left, ind - 1, trange)
        if root.right: self.inorder(root.right, ind + 1, trange)
        return
    
    def BFS(self, root, mindex, res):
        q = collections.deque([(0, root)])
        while q:
            n = len(q)
            for i in range(n):
                temp = q.popleft()
                res[temp[0] - mindex].append(temp[1].val)
                if temp[1].left:
                    q.append((temp[0] - 1, temp[1].left))
                if temp[1].right:
                    q.append((temp[0] + 1, temp[1].right))
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        trange = [0, 0]
        if root:
            self.inorder(root, 0, trange)
        else: return res
        res = [[] for i in range(trange[0], trange[1] + 1)]
        self.BFS(root, trange[0], res) 
        return res
