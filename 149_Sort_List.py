# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def my_sortList(self,head,n):
        if n==0 or n==1: return head
        if n==2:
            temp=head.next
            if temp.val<head.val: #switch the two
                temp.next=head
                head.next=None
                head=temp
                return head
        # do the divide
        half_size=n/2
        temp=head
        for i in range(half_size-1):
            temp=temp.next
        head2=temp.next
        temp.next=None
        head1=self.my_sortList(head,half_size)
        head2=self.my_sortList(head2,n-half_size)
        # conquer, merge two sorted list
        sentinel1,sentinel2=ListNode(0),ListNode(0)
        sentinel1.next=head1
        sentinel2.next=head2
        move1,move2=sentinel1,sentinel2
        while move1.next!=None and move2.next!=None:
            if move1.next.val>move2.next.val:
                # add move2.next to move1.next
                temp1=move2.next
                move2.next=temp1.next # remove move2.next
                temp2=move1.next
                move1.next=temp1
                temp1.next=temp2
            move1=move1.next
        if move1.next==None:
            move1.next=move2.next
        return sentinel1.next
    
    def sortList(self, head):
        #merge sort
        temp=head
        n=0
        while temp!=None:
            n+=1
            temp=temp.next
        head=self.my_sortList(head,n)
        return head
