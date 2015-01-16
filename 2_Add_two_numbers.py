# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result=ListNode(0)
        current=result
        carry=0
        while l1!=None or l2!=None:
            if l1==None:
                temp1=0
            else:
                temp1=l1.val
            if l2==None:
                temp2=0
            else:
                temp2=l2.val
            if temp1+temp2+carry<10:
                current.next=ListNode(temp1+temp2+carry)
                carry=0
            else:
                current.next=ListNode(temp1+temp2+carry-10)
                carry=1
            if l1: l1=l1.next
            if l2: l2=l2.next
            current=current.next
        if carry==1: current.next=ListNode(1)
        return result.next
