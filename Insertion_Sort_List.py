# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head: return head
        sentinel=ListNode(0)
        sentinel.next=head
        to_change=head
        while to_change.next:
            if to_change.next.val<to_change.val:
                temp=sentinel
                while temp.next.val<to_change.next.val:
                    temp=temp.next
            # add to_change after temp
                temp2=to_change.next
                to_change.next=temp2.next
                temp3=temp.next
                temp.next=temp2
                temp2.next=temp3
            else:
                to_change=to_change.next
        return sentinel.next
