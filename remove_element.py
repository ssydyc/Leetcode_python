'''
Created on Jan 26, 2014

@author: songsi
'''
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A)==0: return 0
        removed=0
        for i in range(0,len(A)):
            if A[i]==elem:
                while A[len(A)-1-removed]==elem and i<=len(A)-1-removed: 
                    removed+=1
                if i>=len(A)-1-removed: return i
                A[i]=A[len(A)-1-removed]
                A[len(A)-1-removed]=elem
                removed+=1
        return len(A)-removed
    
    
test=Solution()
print test.removeElement([4,5], 4)