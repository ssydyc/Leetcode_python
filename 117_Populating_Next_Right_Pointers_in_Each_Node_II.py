# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#################################################
# Solution 1, with BFS, O(N) Space & O(N) Time
#################################################

from collections import deque

class Solution(object):
    def connect(self, root):
        if not root: return
        q = deque([root])
        while q:
            prev = None     # the previous node
            for _ in range(len(q)):
        		cur = q.popleft()
        		if cur.left: q.append(cur.left)
        		if cur.right: q.append(cur.right)
        		if not prev: prev = cur
        		else: 
        		    prev.next = cur
        		    prev = cur
        return

#################################################
# Solution 2, recursion, O(logN) Space & O(N) Time
#################################################

class Solution(object):
   def connect(self, root):
    	if root is None: return
    	cur = root.next
    	while cur:
    		if cur.left: 
    			cur = cur.left
    			break
    		elif cur.right:
    			cur = cur.right
    			break
    		else:
    			cur = cur.next
    	if root.right: root.right.next = cur
    	if root.left:
    		root.left.next = root.right if root.right else cur
    	self.connect(root.right)
    	self.connect(root.left)

#################################################
# Solution 3, iterative, O(1) Space & O(N) Time
#################################################

class Solution(object):
   def connect(self, root):
    	cur = root # current node to process
    	hlevel, prev = root, None
    	# hlevel records head node for each level, prev is the previous node
    	while cur:
    		while cur:
    			if cur.left:
    				if prev:
    					prev.next = cur.left
    					prev = prev.next
    				else:
    					prev = cur.left
    					hlevel = cur.left
    			if cur.right:
    				if prev:
    					prev.next = cur.right
    					prev = prev.next
    				else:
    					prev = cur.right
    					hlevel = cur.right
    			cur = cur.next
    		# move to next level
    		cur = hlevel
    		hlevel, prev = None, None
