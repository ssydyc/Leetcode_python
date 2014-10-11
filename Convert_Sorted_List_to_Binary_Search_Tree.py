# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def my_sortedListToBST(self,current,n):
        if n==0: return None
        root=TreeNode(0)
        root.left=self.my_sortedListToBST(current,(n-1)/2)
        root.val=current[0].val
        current[0]=current[0].next
        root.right=self.my_sortedListToBST(current,n-1-(n-1)/2)
        return root
        
    def sortedListToBST(self, head):
        n=0
        current=head;
        while current!=None:
            current=current.next
            n+=1
        return self.my_sortedListToBST([head],n)
