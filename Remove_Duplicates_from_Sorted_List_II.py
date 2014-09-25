# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        myhead=ListNode(0)
        myhead.next=head
        if head==None: return head
        first=myhead
        second=head
        third=head.next # we need three nodes now
        to_delete=None #record the value that needs to be deleted
        while second.next!=None:
            if second.val==third.val:
                to_delete=second.val
                second.next=third.next
                third=second.next
            else:
                if second.val==to_delete: # we need to delete the second one
                    first.next=third
                    second=first.next
                    third=second.next
                else:
                    first=first.next
                    second=second.next
                    third=third.next
        if second.val==to_delete: first.next=third
        return myhead.next
        
