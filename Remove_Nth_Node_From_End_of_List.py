'''
Created on Jan 23, 2014

@author: songsi
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        front=behind=head;
        temp_n=n
        while temp_n>=0:
            front=front.next
            temp_n-=1
            if front==None: break
        if front==None: return head.next
        while front!=None:
            behind=behind.next
            front=front.next
        behind.next=behind.next.next
        return head