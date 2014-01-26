'''
Created on Jan 26, 2014

@author: songsi
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A==[]: return len(A)
        i=j=0
        while j<len(A):
            if A[i]==A[j]: pass
            else:
                i+=1
                A[i]=A[j]
            j+=1
        print A[0:i+1]
        return i+1        
    
test=Solution()
print test.removeDuplicates([1,1,1,2,2,2,3,3])