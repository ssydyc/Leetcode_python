
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        my_head=ListNode(-1)
        move=my_head
        move.next=head
        while move.next!=None and move.next.next!=None:
            temp=move.next.next.next
            temp1=move.next
            temp2=move.next.next
            move.next=temp2
            move.next.next=temp1
            temp1.next=temp
            move=temp1
        return my_head.next
            