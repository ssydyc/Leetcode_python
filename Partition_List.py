# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        myhead=ListNode(0)
        myhead.next=head
        cur=head
        bigger=myhead
        small=myhead
        while cur!=None:
            if cur.val>=x: # no problem bigger one
                bigger=bigger.next
                cur=cur.next
            else: #move cur to smaller one
                cur=cur.next
                temp=bigger.next
                bigger.next=temp.next #remove the smaller one
                temp2=small.next
                small.next=temp
                temp.next=temp2  #add to front
                if small==bigger:
                    small=small.next
                    bigger=bigger.next
                else:
                    small=small.next
        return myhead.next
                
