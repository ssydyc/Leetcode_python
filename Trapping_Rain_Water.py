'''
Created on Jan 25, 2014

@author: songsi
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A)<=2: return 0
        B=A[0:len(A)-1]
        left_max=B.index(max(B))
        if left_max!=0: return self.trap(A[0:left_max+1])+self.trap(A[left_max:len(A)])
        C=A[1:len(A)]
        right_max=C.index(max(C))+1
        if left_max==0 and right_max==len(A)-1: return self.capture(0, len(A)-1, A)
        else: return self.trap(A[0:right_max+1])+self.trap(A[right_max:len(A)])
            
    def capture(self,left,right,A):
        height=min(A[left],A[right])
        result=0
        for i in range(left+1,right):
            result+=max(height-A[i],0)
        return result
 
test=Solution()
print test.trap([5,2,1,2,1,5])           