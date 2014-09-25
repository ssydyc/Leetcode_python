# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        before=head
        if head==None: return head
        else: after=head.next
        while before.next!=None:
            if after.val==before.val:
                #cancel after
                before.next=after.next
                after=before.next
            else:
                #all move forward
                before=before.next
                after=after.next
        return head
