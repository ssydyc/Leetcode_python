# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1==None: return l2
        if l2==None: return l1
        myhead=ListNode(0)
        cur_node=myhead
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                #add l2's node
                temp=l2.next
                cur_node.next=l2
                l2.next=None
                l2=temp
                cur_node=cur_node.next
            else:
                #add l1's node
                temp=l1.next
                cur_node.next=l1
                l1.next=None
                l1=temp
                cur_node=cur_node.next
        if l1==None: cur_node.next=l2
        else: cur_node.next=l1
        return myhead.next
        
