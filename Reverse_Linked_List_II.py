# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m==n: return head
        myhead=ListNode(0)
        myhead.next=head
        start,end=ListNode(0),ListNode(0) #we need start and end to record
        before=myhead
        cur=myhead.next
        before_start=myhead
        i=1
        while i<=n:
            if i==m-1:
                before_start=cur
                before=before.next
                cur=cur.next
            elif i==m:
                start=cur
                before=before.next
                cur=cur.next
            elif i==n:
                end=cur.next
                cur.next=before
                start.next=end
                before_start.next=cur
            elif i>m and i<n:
                temp=cur.next
                cur.next=before
                before=cur
                cur=temp
            else:
                before=before.next
                cur=cur.next
            i+=1    
        return myhead.next
                
                
