# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k==0 or k==1: return head
        if head==None: return head
        my_head=ListNode(-1)
        my_head.next=head
        move=my_head
        tail=self.move_k(move,k)
        while tail!=None:
            next_move=move.next
            temp1=move.next
            move.next=tail
            tail=tail.next
            temp2=temp1.next
            temp1.next=tail
            #reverse the k elments between move and tail
            for i in range(0,k-1):
                temp=temp2.next
                temp2.next=temp1
                temp1=temp2
                temp2=temp
            move=next_move
            tail=self.move_k(move,k)
        return my_head.next
        
    def move_k(self,move,k):
        while k>0:
            if move==None: break
            move=move.next
            k-=1
        return move
         
test=Solution()
temp=[1,2,3,4,5]
head=ListNode(temp[0])
myhead=head
for i in range(1,len(temp)):
    head.next=ListNode(temp[i])
    head=head.next
myhead=test.reverseKGroup(myhead, 2)
while myhead!=None:
    print myhead.val
    myhead=myhead.next     
        
        
        
        
        
        
        
        
    
        