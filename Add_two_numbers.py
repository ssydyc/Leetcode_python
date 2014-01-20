'''
Created on Jan 19, 2014

@author: songsi
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
         
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1==None: return l2
        if l2==None: return l1
        l3=ListNode(l1.val+l2.val)
        temp1=l3
        l1=l1.next
        l2=l2.next
        while l1!=None and l2!=None:
            temp2=ListNode(l1.val+l2.val)
            temp1.next=temp2
            temp1=temp2
            l1=l1.next
            l2=l2.next
        if l1==None:
            while l2!=None:
                temp2=ListNode(l2.val)
                temp1.next=temp2
                temp1=temp2
                l2=l2.next
        else:
            while l1!=None:
                temp2=ListNode(l1.val)
                temp1.next=temp2
                temp1=temp2
                l1=l1.next
        temp1=l3
        exceeds=0
        while temp1.next!=None:
            temp1.val=temp1.val+exceeds
            if temp1.val>=10:
                exceeds=1
                temp1.val-=10
            else: exceeds=0
            temp1=temp1.next
        temp1.val=temp1.val+exceeds
        if temp1.val>=10:
            temp1.val-=10
            temp2=ListNode(1)
            temp1.next=temp2
        return l3       
        