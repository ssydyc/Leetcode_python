class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        result=ListNode(-1)
        head=result
        if lists==[]: return None
        compare=[]
        for temp in lists:
            if temp==None: compare.append('')
            else: compare.append(temp.val)
        small_index=self.mycompare(compare)
        while self.mycompare(compare)!=-1: #not
            head.next=lists[small_index]
            head=head.next
            lists[small_index]=lists[small_index].next
            if lists[small_index]==None: compare[small_index]=''
            else: compare[small_index]=lists[small_index].val
            small_index=self.mycompare(compare)
        head.next=None
        return result.next
    
    
    def mycompare(self,compare):
        min_index=-1
        mymin=''
        for i in range(0,len(compare)):
            if mymin=='' and compare[i]=='': pass
            elif mymin=='' and compare[i]!='':
                mymin=compare[i]
                min_index=i
            else:
                if compare[i]<mymin:
                    mymin=compare[i]
                    min_index=i

        return min_index 