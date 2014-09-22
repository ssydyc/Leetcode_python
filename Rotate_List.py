# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        cur=head
        if cur==None: return head
        tol_len=0
        while cur!=None:
            cur=cur.next
            tol_len+=1
        k=k%tol_len #don't let k exceed tol_len
        k=tol_len-k-1 # pinpoint to kth place
        cur=head #start over again
        while k>0 and cur!=None:
            k-=1
            cur=cur.next
        #now we have the kth node cur
        if cur==None: return head # no be able to do that
        start=cur.next
        cur.next=None
        if start==None: return head
        cur=start
        while start.next!=None:
            start=start.next
        start.next=head
        return cur
