'''
Created on Feb 3, 2014

@author: songsi
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A==[]: return [-1,-1]
        l=-1
        r=len(A)-1
        if A[0]==target: lresult=0
        else:
            while l+1<r:
                m=(l+r)/2
                if A[m]<target:
                    l=m
                else:
                    r=m
            if A[r]!=target: return [-1,-1]
            lresult=r
        l=0
        r=len(A)
        if A[r-1]==target: rresult=r-1
        else:
            while l+1<r:
                m=(l+r)/2
                if A[m]>target:
                    r=m
                else:
                    l=m
            rresult=l
        return [lresult,rresult]
    
    
test=Solution()
print test.searchRange([1,2,2], 2)